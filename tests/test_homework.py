import os
import pytest
import homework
from homework import *


def test_r1_is_even():
    assert is_even(4) is True


def test_r2_can_vote():
    assert can_vote(18) is True


def test_r3_safe_ratio():
    assert safe_ratio(5, 0) == 0


def test_r4_last_item():
    assert last_item([]) is None


def test_r5_verify_token():
    assert verify_token("secret_token_999") is False
