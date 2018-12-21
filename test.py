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

from tinderhandler import Tinder

handler = Tinder()
user_profiles = handler.get_endpoint("user/recs", {})
print("Before:")
for user in user_profiles['results']:
    print(user['_id'])
for user in user_profiles['results']:
    handler.get_endpoint('like/' + user['_id'], {})
user_profiles = handler.get_endpoint("user/recs", {})
print("After:")
for user in user_profiles['results']:
    print(user['_id'])
