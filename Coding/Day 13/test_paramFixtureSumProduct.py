'''
Name: Abhigyan Maji
ID: 30382
Date: 21 July 2025
Purpose: Demonstrate class-based tests with parametrized fixture for sum and product validations
'''

from pytest import fixture
from functools import reduce

@fixture(params=[(1, 2, 3), (3, 2, 1)])
def sampleData(request):
    print('setup class scoped...')
    yield request.param
    print('teardown class scoped...')

class TestClassOne:
    def test_One(self, sampleData):
        print(f'\ntestOne()...with {sampleData}')
        assert sum(sampleData) == 6

    def test_Two(self, sampleData):
        print(f'\ntestTwo()...with {sampleData}')
        assert reduce(lambda x, y: x * y, sampleData) == 6
