'''
Name: Abhigyan Maji
ID: 30382
Date: 22 July 2025
Purpose: Custom pytest configuration using addoption and fixtures for --env and --exam command-line options.
'''

def pytest_addoption(parser):
    print('Inside pytest_addoption()')
    parser.addoption(
        '--env', action='store', default='dev', help='Environment is dev/staging/prod'
    )
    parser.addoption(
        '--exam', action='store', default='alpha', help='Test Environment is unit/alpha/beta'
    )

import pytest

@pytest.fixture
def env(request):
    print('\nInside env() fixture')
    return request.config.getoption('--env')

@pytest.fixture
def exam(request):
    print('\nInside exam() fixture')
    return request.config.getoption('--exam')
