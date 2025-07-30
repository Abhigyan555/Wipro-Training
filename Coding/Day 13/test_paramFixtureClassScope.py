'''
Name: Abhigyan Maji
ID: 30382
Date: 21 July 2025
Purpose: Demonstrate class-scoped parametrized fixture with pytest
'''

from pytest import fixture

@fixture(params=[([1, 2, 3], 6), ([3, 2, 1], 6), ([2, 3, 5], 10)])
def sampleData(request):
    print('\nsetup class scoped...')
    yield request.param
    print('teardown class scoped...')
    print('*' * 40)

class TestClassOne:
    def test_One(self, sampleData):
        col, res = sampleData
        print(f'\ntestOne()...with col: {col} and res: {res}')
        assert sum(col) == res
