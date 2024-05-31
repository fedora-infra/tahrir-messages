# SPDX-FileCopyrightText: 2024 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""Unit tests for the message schema."""

import pytest
from jsonschema import ValidationError

from tahrir_messages import BadgeAwardV1, PersonLoginFirstV1, PersonRankAdvanceV1

from .utils import DUMMY_BADGE, DUMMY_PERSON, DUMMY_USER


def test_person_login_first():
    body = {
        "user": DUMMY_USER,
    }
    message = PersonLoginFirstV1(body=body)
    message.validate()

    expected_summary = "dudemcpants logged into badges for the first time"
    assert message.topic == "badges.person.login.first"
    assert message.summary == expected_summary
    assert str(message) == expected_summary
    assert message.agent_name == "dudemcpants"
    assert message.usernames == ["dudemcpants"]
    assert message.app_name == "tahrir"
    assert message.url is None
    assert message.app_icon == "https://apps.fedoraproject.org/img/icons/badges.png"


def test_person_login_first_missing_fields():
    message = PersonLoginFirstV1(body={})
    with pytest.raises(ValidationError):
        message.validate()


def test_badge_award():
    body = {"user": DUMMY_USER, "badge": DUMMY_BADGE}
    message = BadgeAwardV1(body=body)
    message.validate()

    expected_summary = "dudemcpants was awarded the badge `White Hat`"
    assert message.topic == "badges.badge.award"
    assert message.summary == expected_summary
    assert str(message) == expected_summary
    assert message.agent_name == "dudemcpants"
    assert message.usernames == ["dudemcpants"]
    assert message.app_name == "tahrir"
    assert message.url is None
    assert message.app_icon == "https://apps.fedoraproject.org/img/icons/badges.png"


def test_badge_award_missing_fields():
    message = BadgeAwardV1(body={})
    with pytest.raises(ValidationError):
        message.validate()

    body = {"badge": DUMMY_BADGE}
    message = BadgeAwardV1(body=body)
    with pytest.raises(ValidationError):
        message.validate()

    body = {"user": DUMMY_BADGE}
    message = BadgeAwardV1(body=body)
    with pytest.raises(ValidationError):
        message.validate()


def test_person_rank_advance():
    body = {"old_rank": 2, "person": DUMMY_PERSON}
    message = PersonRankAdvanceV1(body=body)
    message.validate()

    expected_summary = "aaronhale's Badges rank changed from 2 to 1"
    assert message.topic == "badges.person.rank.advance"
    assert message.summary == expected_summary
    assert str(message) == expected_summary
    assert message.agent_name == "aaronhale"
    assert message.usernames == ["aaronhale"]
    assert message.app_name == "tahrir"
    assert message.url is None
    assert message.app_icon == "https://apps.fedoraproject.org/img/icons/badges.png"


def test_person_rank_advance_missing_fields():
    """Assert an exception is actually raised on validation failure."""
    message = BadgeAwardV1(body={})
    with pytest.raises(ValidationError):
        message.validate()
