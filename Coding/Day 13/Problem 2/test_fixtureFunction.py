"""
Name: Abhigyan Maji
ID: 30382
Date: 21 July 2025
Purpose: Test sum and product using shared fixture functions
"""
def test_sum(sumData):
    data, result = sumData
    assert sum(data) == result

def test_product(prodData):
    data, result = prodData
    prod = 1
    for i in data:
        prod *= i
    assert prod == result