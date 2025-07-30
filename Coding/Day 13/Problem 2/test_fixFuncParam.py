"""
Name: Abhigyan Maji
ID: 30382
Date: 21 July 2025
Purpose: Parametrized test functions for sum and product
"""
def test_param_sum(sumDataFix):
    data, expected = sumDataFix
    assert sum(data) == expected

def test_param_product(prodDataFix):
    data, expected = prodDataFix
    result = 1
    for x in data:
        result *= x
    assert result == expected