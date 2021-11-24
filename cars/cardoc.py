import requests
from requests.exceptions import HTTPError

from django.http import JsonResponse


class CardocAPI:
    def __init__(self):
        self.reqeust_url = "https://dev.mycar.cardoc.co.kr/v1/trim/"

    def get_trim_information(self, trim_id):
        try:
            response = requests.get(self.reqeust_url + str(trim_id), timeout=3)

            response.raise_for_status()

            return response.json()

        except HTTPError:
            return None
