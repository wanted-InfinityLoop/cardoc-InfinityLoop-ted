from django.http import response
import bcrypt
import json
import jwt

from django.test import TestCase, Client
from unittest.mock import patch, MagicMock

from users.models import CarOwner, User
from cars.models import TirePosition, Tire, Car
from my_settings import MY_SECRET_KEY, ALGORITHM


class CarViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        user = User.objects.create(
            id="test1234",
            password=bcrypt.hashpw("abcd1234!@".encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
        )
        user_2 = User.objects.create(
            id="test5678",
            password=bcrypt.hashpw("abcd1234!@".encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
        )

        self.access_token = jwt.encode({"user_id": user.id}, MY_SECRET_KEY, ALGORITHM)
        self.access_token_2 = jwt.encode({"user_id": user_2.id}, MY_SECRET_KEY, ALGORITHM)

        TirePosition.objects.bulk_create([TirePosition(id=1, name="전방"), TirePosition(id=2, name="후방")])

        Tire.objects.bulk_create(
            [
                Tire(id=1, tire_position_id=1, width=200, aspect_ratio=58, wheel_size=15),
                Tire(id=2, tire_position_id=2, width=200, aspect_ratio=58, wheel_size=15),
            ]
        )

        Car.objects.create(id=1, model_name="제네시스 GV70", front_tire_id=1, rear_tire_id=2)

        CarOwner.objects.create(user_id="test1234", car_id=1)

    @patch("cars.cardoc.requests")
    def test_post_car_success(self, mocked_requests):
        class MockedResponse:
            def __init__(self, status_code):
                self.status_code = status_code

            def json(self):
                return {
                    "modelName": "오피러스",
                    "trimName": "GH270 고급형",
                    "spec": {
                        "driving": {
                            "frontTire": {"name": "타이어 전", "value": "225/60R16", "unit": "", "multiValues": ""},
                            "rearTire": {"name": "타이어 후", "value": "225/60R16", "unit": "", "multiValues": ""},
                        }
                    },
                }

            def raise_for_status(self):
                pass

        data = [
            {"id": "test1234", "trimId": 5000},
        ]

        mocked_requests.get = MagicMock(return_value=MockedResponse(200))
        response = self.client.post("/cars", json.dumps(data), content_type="application/json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"results": [{"User": "test1234", "message": "Register 오피러스 GH270 고급형"}]},
        )

    @patch("cars.cardoc.requests")
    def test_post_car_invalid_trim_value(self, mocked_requests):
        class MockedResponse:
            def __init__(self, status_code):
                self.status_code = status_code

            def json(self):
                return None

            def raise_for_status(self):
                return None

        data = [
            {"id": "test1234", "trimId": "?"},
        ]

        mocked_requests.get = MagicMock(return_value=MockedResponse(400))
        response = self.client.post("/cars", json.dumps(data), content_type="application/json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"results": [{"User": "test1234", "message": "INVALID_TRIM_VALUE"}]},
        )

    @patch("cars.cardoc.requests")
    def test_post_car_invalid_tire_info_format(self, mocked_requests):
        class MockedResponse:
            def __init__(self, status_code):
                self.status_code = status_code

            def json(self):
                return {
                    "modelName": "오피러스",
                    "trimName": "GH270 고급형",
                    "spec": {
                        "driving": {
                            "frontTire": {"name": "타이어 전", "value": "225,60,16", "unit": "", "multiValues": ""},
                            "rearTire": {"name": "타이어 후", "value": "225,60,16", "unit": "", "multiValues": ""},
                        }
                    },
                }

            def raise_for_status(self):
                return None

        data = [
            {"id": "test1234", "trimId": 5000},
        ]

        mocked_requests.get = MagicMock(return_value=MockedResponse(200))
        response = self.client.post("/cars", json.dumps(data), content_type="application/json")

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {"message": "INVALID_TIRE_INFO_FORMAT"},
        )

    @patch("cars.cardoc.requests")
    def test_post_car_key_error(self, mocked_requests):
        class MockedResponse:
            def __init__(self, status_code):
                self.status_code = status_code

            def json(self):
                return {
                    "modelName": "오피러스",
                    "trimName": "GH270 고급형",
                    "spec": {
                        "driving": {
                            "frontTire": {"name": "타이어 전", "value": "225/60R16", "unit": "", "multiValues": ""},
                            "rearTire": {"name": "타이어 후", "value": "225/60R16", "unit": "", "multiValues": ""},
                        }
                    },
                }

            def raise_for_status(self):
                return None

        data = [
            {"id": "test1234", "trim_id": 5000},
        ]

        mocked_requests.get = MagicMock(return_value=MockedResponse(200))
        response = self.client.post("/cars", json.dumps(data), content_type="application/json")

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {"message": "KEY_ERROR"},
        )

    @patch("cars.cardoc.requests")
    def test_post_car_key_error(self, mocked_requests):
        class MockedResponse:
            def __init__(self, status_code):
                self.status_code = status_code

            def json(self):
                return {
                    "modelName": "오피러스",
                    "trimName": "GH270 고급형",
                    "spec": {
                        "driving": {
                            "frontTire": {"name": "타이어 전", "value": "225/60R16", "unit": "", "multiValues": ""},
                            "rearTire": {"name": "타이어 후", "value": "225/60R16", "unit": "", "multiValues": ""},
                        }
                    },
                }

            def raise_for_status(self):
                return None

        data = [
            {"id": "test1235", "trimId": 5000},
        ]

        mocked_requests.get = MagicMock(return_value=MockedResponse(200))
        response = self.client.post("/cars", json.dumps(data), content_type="application/json")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json(),
            {"message": "USER_DOES_NOT_EXIST"},
        )

    def test_get_car_info_success(self):
        header = {"HTTP_Authorization": f"Bearer {self.access_token}"}

        response = self.client.get("/cars/users/tire", content_type="application/json", **header)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "results": [
                    {
                        "model_name": "제네시스 GV70",
                        "front_tire": {"width": 200, "aspect_ratio": 58, "wheel_size": 15},
                        "rear_tire": {
                            "width": 200,
                            "aspect_ratio": 58,
                            "wheel_size": 15,
                        },
                    }
                ]
            },
        )

    def test_get_car_info_not_found_information(self):
        header = {"HTTP_Authorization": f"Bearer {self.access_token_2}"}

        response = self.client.get("/cars/users/tire", content_type="application/json", **header)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json(),
            {"message": "NOT_FOUND_CAR_INFORMATION"},
        )
