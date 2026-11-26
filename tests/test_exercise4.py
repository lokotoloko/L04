import os
import sqlite3
import pytest
import exercise4
from exercise4 import *


def test_r1_hardcoded_admin_password():
    assert check_admin("admin123") is False


def test_r2_find_user_sql_injection():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT)")
    db.execute("INSERT INTO users VALUES ('alice')")
    assert find_user(db, "' OR '1'='1") is None
