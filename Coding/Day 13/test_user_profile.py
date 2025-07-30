"""
Name: Abhigyan Maji
ID: 30382
Date: 21 July 2025
Purpose: Use dictionary fixtures to test user profile
"""
import pytest

@pytest.fixture
def username():
    return "admin"

@pytest.fixture
def userProfile(username):
    return {"user": username, "role": "admin"}

def test_user_profile(userProfile):
    assert userProfile["user"] == "admin"
    assert userProfile["role"] == "admin"