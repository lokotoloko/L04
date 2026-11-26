import os
import sqlite3
import subprocess

import pytest

import exercise3
from exercise3 import *


# bug report 1
def average(numbers):
    """Average of a list. An empty list has average 0"""
    return sum(numbers) / len(numbers) if numbers else 0


def first_word(text):
    """The first word of the text, or "" if the text is empty"""
    return text.split()[0]


def percent(part, total):
    """part as a percentage of total. If total is 0, the result is 0"""
    return part / total * 100 if total else 0


# bug report 2
def first_word(text):
    """The first word of the text, or "" if the text is empty"""
    return text.strip() if not text.strip() else text.split()[0]


# bug report 3
def average(numbers):
    """Average of a list. An empty list has average 0"""
    return sum(numbers) / len(numbers)


def first_word(text):
    """The first word of the text, or "" if the text is empty"""
    return text.split()[0]


def percent(part, total):
    """part as a percentage of total. If total is 0, the result is 0"""
    if total == 0:
        return 0
    return part / total * 100
