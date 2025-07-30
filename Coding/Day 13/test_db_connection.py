"""
Name: Abhigyan Maji
ID: 30382
Date: 21 July 2025
Purpose: Test mock database connection using fixture
"""
import pytest

@pytest.fixture
def dbConnection():
    return "MockDBConnection"

def test_connection(dbConnection):
    assert dbConnection is not None