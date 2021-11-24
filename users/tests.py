import json
import bcrypt
import jwt

from django.test import TestCase, Client

from users.models import User
from my_settings import MY_SECRET_KEY, ALGORITHM


class SignupViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        User.objects.create(id="테스트유저", password="abcd12!@")

    def tearDown(self):
        User.objects.all().delete()

    def test_post_signup_success(self):
        data = {"id": "테스트유저2", "password": "abcd12!@"}

        response = self.client.post(
            "/users/signup", json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "User 테스트유저2 has created!"})

    def test_post_signup_registered_id(self):
        data = {"id": "테스트유저", "password": "abcd12!@"}

        response = self.client.post(
            "/users/signup", json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "REGISTERED_ID"})

    def test_post_signup_invalid_id(self):
        data = {"id": "", "password": "abcd12!@"}

        response = self.client.post(
            "/users/signup", json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "INVALID_ID_FORMAT"})

    def test_post_signup_invalid_password_format(self):
        data = {"id": "테스트유저2", "password": "abcd12"}

        response = self.client.post(
            "/users/signup", json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "INVALID_PASSWORD_FORMAT"})

    def test_post_signup_key_error(self):
        data = {"password": "abcd12"}

        response = self.client.post(
            "/users/signup", json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "KEY_ERROR"})


class SigninViewTest(TestCase):
    def setUp(self):
        self.cilent = Client()

        user1 = User.objects.create(
            id="테스트유저1",
            password=bcrypt.hashpw("abcd12!@".encode("utf-8"), bcrypt.gensalt()).decode(
                "utf-8"
            ),
        )

        self.access_token1 = jwt.encode({"user_id": user1.id}, MY_SECRET_KEY, ALGORITHM)

    def tearDown(self):
        User.objects.all().delete()

    def test_post_signin_success(self):
        data = {"id": "테스트유저1", "password": "abcd12!@"}

        response = self.client.post(
            "/users/signin", json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"message": "User 테스트유저1 has signed in!", "token": self.access_token1},
        )

    def test_post_signin_invalid_auth_request_id(self):
        data = {"id": "테스트유저2", "password": "abcd12!@"}

        response = self.client.post(
            "/users/signin", json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "INVALID_AUTH_REQUEST"})

    def test_post_signin_invalid_auth_request_password(self):
        data = {"id": "테스트유저1", "password": "abcd12!"}

        response = self.client.post(
            "/users/signin", json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "INVALID_AUTH_REQUEST"})

    def test_post_signin_key_error(self):
        data = {"password": "abcd12!"}

        response = self.client.post(
            "/users/signin", json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "KEY_ERROR"})
