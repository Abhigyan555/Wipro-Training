"""
Name: Abhigyan Maji
ID: 30382
Date: 21 July 2025
Purpose: Shared fixtures for sum and product tests with parameters
"""
import pytest

@pytest.fixture
def sumData():
    return ([1, 2, 3], 6)

@pytest.fixture
def prodData():
    return ([1, 2, 3], 6)

@pytest.fixture(params=[
    ([1, 2, 3], 6),
    ([2, 2, 2], 6),
    ([3, 1, 2], 6)
])
def sumDataFix(request):
    return request.param

@pytest.fixture(params=[
    ([1, 2, 3], 6),
    ([1, 1, 6], 6),
    ([2, 1, 3], 6)
])
def prodDataFix(request):
    return request.param