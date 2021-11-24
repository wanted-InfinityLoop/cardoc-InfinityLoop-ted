import json
import bcrypt
import jwt

from django.views import View
from django.http import JsonResponse

from users.models import User
from core.validation import password_validator
from my_settings import MY_SECRET_KEY, ALGORITHM


class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            id = data["id"]
            password = data["password"]

            if User.objects.filter(id=id).exists():
                return JsonResponse({"message": "REGISTERED_ID"}, status=400)

            if not id:
                return JsonResponse({"message": "INVALID_ID_FORMAT"}, status=400)

            if not password_validator(password):
                return JsonResponse({"message": "INVALID_PASSWORD_FORMAT"}, status=400)

            User.objects.create(
                id=id,
                password=bcrypt.hashpw(
                    password.encode("utf-8"), bcrypt.gensalt()
                ).decode("utf-8"),
            )

            return JsonResponse({"message": f"User {id} has created!"}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


class SigninView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not User.objects.filter(id=data["id"]).exists():
                return JsonResponse({"message": "INVALID_AUTH_REQUEST"}, status=400)

            user = User.objects.get(id=data["id"])

            if not bcrypt.checkpw(
                data["password"].encode("utf-8"), user.password.encode("utf-8")
            ):
                return JsonResponse({"message": "INVALID_AUTH_REQUEST"}, status=400)

            access_token = jwt.encode({"user_id": user.id}, MY_SECRET_KEY, ALGORITHM)

            return JsonResponse(
                {"message": f"User {user.id} has signed in!", "token": access_token},
                status=200,
            )

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
