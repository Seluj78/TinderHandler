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

import re

import requests
import robobrowser

from tinderhandler._const import FB_AUTH_URL, MOBILE_USER_AGENT


def _get_fb_token(fb_email: str, fb_password: str) -> str:
    """
    Gets an access token from a username and password from facebook.

    :param fb_email: The user's email
    :param fb_password: The user's password

    :return: Returns an access token
    """

    s = robobrowser.RoboBrowser(user_agent=MOBILE_USER_AGENT, parser="lxml")
    s.open(FB_AUTH_URL)
    f = s.get_form()
    f["pass"] = fb_password
    f["email"] = fb_email
    s.submit_form(f)
    f = s.get_form()
    try:
        s.submit_form(f, submit=f.submit_fields['__CONFIRM__'])
        access_token = re.search(
            r"access_token=([\w\d]+)", s.response.content.decode()).groups()[0]
        return str(access_token)
    except Exception as ex:
        raise ValueError("access token could not be retrieved. Check your username and password. "
                         "Official error: %s" % ex)


def _get_fb_id(fb_access_token: str) -> str:
    """
    Gets a facebook user ID from an facebook access token

    :param fb_access_token: The facebook access token

    :return: Returns the user's id
    """

    req = requests.get(
        'https://graph.facebook.com/me?access_token=' + fb_access_token)
    return str(req.json()["id"])
