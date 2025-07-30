"""
Name: Abhigyan Maji
ID: 30382
Date: 21 July 2025
Purpose: Shared state fixture to test sum and product of a list
"""
import pytest

@pytest.fixture
def sampleData():
    return [1, 2, 3]

def test_sum(sampleData):
    assert sum(sampleData) == 6

def test_product(sampleData):
    result = 1
    for i in sampleData:
        result *= i
    assert result == 6