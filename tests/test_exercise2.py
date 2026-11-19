import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_is_passing_boundary():
    assert is_passing(5) == True


# bug report 2
def test_r2_is_valid_password_boundary():
    assert is_valid_password("abcdefg1") == True


# bug report 3
def test_r3_clamp_boundary():
    assert clamp(10, 1, 5) == 5
