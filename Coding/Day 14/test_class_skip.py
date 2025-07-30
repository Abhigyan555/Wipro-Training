'''
Name: Abhigyan Maji
ID: 30382
Date: 22 July 2025
Purpose: Demonstrate skipping an entire test class using @pytest.mark.skip.
'''

import pytest 

@pytest.mark.skip(reason='Trying to skip the whole class')
class TestClass:
    def test_One(self):
        print('test_One() from TestClass... ')

    def test_Two(self):
        print('test_Two() from TestClass... ')

    def test_Three(self):
        print('test_Three() from TestClass... ')
