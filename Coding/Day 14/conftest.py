'''
Name: Abhigyan Maji
ID: 30382
Date: 22 July 2025
Purpose: Custom pytest options using addoption and fixtures
'''

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment: dev/staging/prod")

import pytest

@pytest.fixture
def env(request):
    return request.config.getoption("--env")
