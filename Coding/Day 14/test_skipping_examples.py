'''
Name: Abhigyan Maji
ID: 30382
Date: 22 July 2025
Purpose: Demonstrate different ways to skip tests using pytest.
'''

import pytest 
import sys 

# Simple skip 
@pytest.mark.skip(reason='Functionality not implemented')
def test_funOne():
    pass 
		
# Conditional skip
@pytest.mark.skipif(sys.platform != 'linux', reason='Specifically written for Linux')
def test_funTwo():
    pass 

# Programmatic skip (inside the test function)
def test_funThree():
    if 4 == 3 + 1:
        pytest.skip('Skipping funThree')	
    assert False
