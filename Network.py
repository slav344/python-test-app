import json

import requests

from CatResponse import CatResponse
from UserResponse import UserResponse


class NetworkProvider:
    try:
        response = requests.get("https://catfact.ninja/fact")
        cat_response = CatResponse.from_json(json.dumps(response.json()))
    except:
        cat_response = "ERROR!"

    def get_result(self):
        return self.cat_response


class UserController:
    try:
        response = requests.get("https://randomuser.me/api/")
        user_response = UserResponse.from_json(json.dumps(response.json()))
    except:
        user_response = "ERROR!"

    def get_result(self):
        return self.user_response
