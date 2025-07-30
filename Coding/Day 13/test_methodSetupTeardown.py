'''
Name: Abhigyan Maji
ID: 30382
Date: 21 July 2025
Purpose: Demonstrate method-level setup and teardown in pytest with basic add and sub test cases
'''

class TestExampleOne:
    def setup_method(self):
        # Setup method runs before each test
        self.testAddData = [
            (2, 3, 5),
            (-8, 3, -5),
            (0, 20, 20)
        ]

    def teardown_method(self):
        # Teardown method runs after each test
        self.testAddData = []

    def test_add(self):
        print('\nAdd method called')
        for x, y, res in self.testAddData:
            assert x + y == res

    def test_sub(self):
        print('\nSub method called')
        assert 8 - 3 == 5
