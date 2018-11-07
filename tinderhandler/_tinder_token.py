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

import json

import requests

from tinderhandler._const import API_HEADERS, API_HOST


def get_tinder_token(fb_access_token, fb_user_id):
    """
    Gets the tinder auth token

    :param fb_access_token: The facebook access token
    :param fb_user_id:  The user's id

    :return: Returns the tinder token or raises an error
    """

    url = API_HOST + "/auth"
    req = requests.post(url,
                        headers=API_HEADERS,
                        data=json.dumps(
                            {'facebook_token': fb_access_token, 'facebook_id': fb_user_id})
                        )
    try:
        tinder_auth_token = req.json()["token"]
        API_HEADERS.update({"X-Auth-Token": tinder_auth_token})
        return tinder_auth_token
    except Exception as e:
        raise e
