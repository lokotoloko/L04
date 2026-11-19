import os
import sqlite3
import subprocess

import pytest

import exercise1
from exercise1 import *


# bug report 1
def test_r1_is_even_even_number():  
    assert is_even(4) == True


# bug report 2
def test_r2_rectangle_area_product_5_by_3():
    assert rectangle_area(5, 3) == 15


# bug report 3
def test_r3_double_boundary_5():
    assert double(5) == 10
