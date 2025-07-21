'''
Name: Abhigyan Maji
ID: 30382
Date: 18 July 2025  
Purpose: Creating test cases
''' 

import pytest
from arithmeticFun import add, sub, mult, divf

def test_AddFirst():
    assert add(10, 20) == 30

def test_AddSecond():
    assert add(10, -20) == -10

def test_SubFirst():
    assert sub(10, -20) == 30

def test_SubSecond():
    assert sub(100, 20) == 80

def test_Mult():
    assert mult(5, 4) == 20

def test_Divf():
    assert divf(20, 5) == 4.0

def test_DivfZero():
    with pytest.raises(ZeroDivisionError):
        divf(10, 0)
