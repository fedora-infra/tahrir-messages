# SPDX-FileCopyrightText: 2024 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""Utilities for the unit tests."""


DUMMY_USER = {
    "username": "dudemcpants",
    "badges_user_id": 123456,
}

DUMMY_BADGE = {
    "badge_id": "white-hat",
    "description": "You submitted a bodhi update with type security",
    "image_url": "https://badges.fedoraproject.org/pngs/white-hat.png",
    "name": "White Hat",
}

DUMMY_PERSON = {
    "bio": None,
    "email": "aaronhale@fedoraproject.org",
    "id": 1234,
    "nickname": "aaronhale",
    "rank": 1,
    "website": None,
}
