'''
Name: Abhigyan Maji
ID: 30382
Date: 22 July 2025
Purpose: Use subprocess to run external Python file and verify output via assertions.
'''

import subprocess

def test_First():
    res = subprocess.run(['python', 'first.py', 'filename.txt'], capture_output=True, text=True)
    print(res.stdout)
    resString = '__main__  printing from funFirst()'
    assert resString in res.stdout

def test_Second():
    res = subprocess.run(['python', 'first.py', 'filename.txt'], capture_output=True, text=True)
    print(res.stdout)
    resString = '__main__'
    assert resString in res.stdout

def test_Third():
    res = subprocess.run(['python', 'first.py', 'filename.txt'], capture_output=True, text=True)
    print(res.stdout)
    resString = 'printing'
    assert resString in res.stdout
