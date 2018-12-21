# coding=utf-8

"""
    TinderHandler - A Python library to access Tinder's API
    Copyright (C) 2018-2019 Jules Lasne jules.lasne@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os
import sys
import json

import requests

from tinderhandler._facebook import _get_fb_token, _get_fb_id
from tinderhandler._tinder_token import get_tinder_token
from tinderhandler._const import API_HEADERS, API_HOST


class Tinder:
    def __init__(self, fb_email=None, fb_password=None, token=None):
        if not token:
            if not fb_password:
                if "FB_PASSWORD" not in os.environ:
                    raise EnvironmentError("Facebook password not set in environement")
                else:
                    self._facebook_password = os.environ.get("FB_PASSWORD")
            else:
                self._facebook_password = fb_password
            if not fb_email:
                if "FB_EMAIL" not in os.environ:
                    raise EnvironmentError("Facebook email not set in environement")
                else:
                    self._facebook_email = os.environ.get("FB_EMAIL")
            else:
                self._facebook_email = fb_email

            self._facebook_token = _get_fb_token(
                self._facebook_email, self._facebook_password
            )
            self._facebook_id = _get_fb_id(self._facebook_token)
            self.tinder_token = get_tinder_token(self._facebook_token, self._facebook_id)
        else:
            self.tinder_token = token
        API_HEADERS.update({"X-Auth-Token": self.tinder_token})

    def get_endpoint(self, endpoint: str, data: dict):
        try:
            url = API_HOST + "/" + endpoint
            r = requests.post(url, headers=API_HEADERS, data=json.dumps(data))
            return r.json()
        except requests.exceptions.RequestException as e:
            print("Something went wrong with getting updates:", e)
            raise e

    def like_batch(self):
        user_profiles = self.get_endpoint("user/recs", {})
        print(f"Found {len(user_profiles['results'])} people.")
        for user in user_profiles['results']:
            self.get_endpoint('like/' + user['_id'], {})
