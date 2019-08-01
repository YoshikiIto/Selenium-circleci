import pytest
import bmi

# ケース１：正常系
def test_case1():
    assert bmi.calc_bmi(170, 65) == 22.5

# ケース２：異常系
def test_case2():
    assert bmi.calc_bmi(0, 65) == 0
