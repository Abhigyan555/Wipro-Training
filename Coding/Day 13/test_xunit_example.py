"""
Name: Abhigyan Maji
ID: 30382
Date: 21 July 2025
Purpose: Demonstrate xUnit style setup and teardown in pytest
"""

def setup_module():
    print("\n[Setup Module] Connecting to DB")

def teardown_module():
    print("\n[Teardown Module] Closing DB")

def setup_function():
    print("\n[Setup Function] Start test")

def teardown_function():
    print("\n[Teardown Function] End test")

def test_case_1():
    print("Running Test Case 1")
    assert True

def test_case_2():
    print("Running Test Case 2")
    assert 5 > 3