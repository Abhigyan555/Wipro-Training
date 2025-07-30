'''
Name: Abhigyan Maji
ID: 30382
Date: 21 July 2025
Purpose: Demonstrate class-level and method-level setup and teardown in pytest with basic add and sub tests
'''

class TestExampleOne:
    @classmethod
    def setup_class(cls):
        print('\nSetup class method called')

    @classmethod
    def teardown_class(cls):
        print('\nTeardown class method called')

    def setup_method(self):
        print('\nSetup method method called')

    def teardown_method(self):
        print('\nTeardown method method called')

    def test_add(self):
        print('\nAdd method called')
        assert 2 + 3 == 5

    def test_sub(self):
        print('\nSub method called')
        assert 8 - 3 == 5
