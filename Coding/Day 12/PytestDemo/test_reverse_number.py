'''
Name: Abhigyan Maji
ID: 30382
Date: 18 July 2025  
Purpose: Creating test cases
''' 
from reverse_number import reverse_number

def test_reverse_number():
    assert reverse_number(123) == 321
    assert reverse_number(400) == 4
    assert reverse_number(1001) == 1001
