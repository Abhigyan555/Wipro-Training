'''
Name: Abhigyan Maji
ID: 30382
Date: 22 July 2025
Purpose: Examples of skipping and xfail tests in pytest
'''

import pytest
import sys

@pytest.mark.skip(reason="Not implemented yet")
def test_skip_demo():
    assert False

@pytest.mark.xfail(reason="Known issue with platform")
def test_expected_fail():
    assert 1 == 2

@pytest.mark.xfail(sys.platform == 'win32', reason="Windows specific fail")
def test_conditional_fail():
    assert False

@pytest.mark.xfail(strict=True, reason="Should fail, if not mark as error")
def test_xfail_strict():
    assert True
