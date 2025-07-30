'''
Name: Abhigyan Maji
ID: 30382
Date: 21 July 2025
Purpose: Demonstrate use of a simple pytest fixture for test data setup
'''

import pytest 

@pytest.fixture 
def sample(): 
    print('Setup Part of my Fixture')
    return 100

def test_funOne(sample):
    print('test_funOne() called')
    assert sample == 100

def test_funTwo(sample):
    print('test_funTwo() called')
    assert sample - 2 == 98
