'''
Name: Abhigyan Maji
ID: 30382
Date: 22 July 2025
Purpose: Test based on custom env argument
'''

def test_envValue(env):
    assert env in ["dev", "staging", "prod"]
