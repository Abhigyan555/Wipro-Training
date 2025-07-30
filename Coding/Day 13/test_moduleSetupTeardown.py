'''
Name: Abhigyan Maji
ID: 30382
Date: 21 July 2025
Purpose: Demonstrate module-level setup and teardown using pytest
'''

def setup_module():
    print('\nsetup module called before any tests')

def teardown_module():
    print('\ntearup module called after all tests')

def test_funOne():
    print('running funOne')
    assert True

def test_funTwo():
    print('\nrunning funTwo')
    assert True

def test_funThree():
    print('\nrunning funThree')
    assert True
