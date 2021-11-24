import json
import re

from django.views import View
from django.http import JsonResponse
from django.db import transaction

from cars.models import Tire, TirePosition, Car
from cars.cardoc import CardocAPI
from users.models import User, CarOwner
from core.utils import login_decorator
from core.validation import tire_format_validator


class CarView(View):
    def get_or_create_car_instance(self, trim_information, front_tire_infos, rear_tire_infos):
        front_tire, _ = Tire.objects.get_or_create(
            tire_position_id=TirePosition.Type.FRONT.value,
            width=front_tire_infos[0],
            aspect_ratio=front_tire_infos[1],
            wheel_size=front_tire_infos[2],
        )

        rear_tire, _ = Tire.objects.get_or_create(
            tire_position_id=TirePosition.Type.REAR.value,
            width=rear_tire_infos[0],
            aspect_ratio=rear_tire_infos[1],
            wheel_size=rear_tire_infos[2],
        )

        car, _ = Car.objects.get_or_create(
            model_name=f"{trim_information['modelName']} {trim_information['trimName']}",
            front_tire=front_tire,
            rear_tire=rear_tire,
        )

        return car

    def post(self, request):
        try:
            datas = json.loads(request.body)
            results = []

            if len(datas) > 5:
                return JsonResponse({"message": "TOO_MANY_REQUEST"}, status=400)

            with transaction.atomic():
                for data in datas:
                    trim_information = CardocAPI().get_trim_information(data["trimId"])
                    user = User.objects.get(id=data["id"])

                    if not trim_information:
                        results.append({"User": user.id, "message": "INVALID_TRIM_VALUE"})
                        continue

                    front_tire_value = trim_information["spec"]["driving"]["frontTire"]["value"]
                    rear_tire_value = trim_information["spec"]["driving"]["rearTire"]["value"]

                    if not (tire_format_validator(front_tire_value) and tire_format_validator(rear_tire_value)):
                        return JsonResponse({"message": "INVALID_TIRE_INFO_FORMAT"}, status=400)

                    front_tire_infos = re.split(r"[/,R]", front_tire_value)
                    rear_tire_infos = re.split(r"[/,R]", rear_tire_value)

                    car = self.get_or_create_car_instance(trim_information, front_tire_infos, rear_tire_infos)

                    if not CarOwner.objects.filter(user_id=user.id, car_id=car.id).exists():
                        CarOwner.objects.create(user_id=User.objects.get(id=data["id"]).id, car_id=car.id)
                        results.append({"User": user.id, "message": f"Register {car.model_name}"})
                    else:
                        results.append({"User": user.id, "message": f"Already Registered {car.model_name}"})

            return JsonResponse({"results": results}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except User.DoesNotExist:
            return JsonResponse({"message": "USER_DOES_NOT_EXIST"}, status=404)
