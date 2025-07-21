'''
Name: Abhigyan Maji
ID: 30382
Date: 17 July 2025  
Purpose: Demonstrate exception logging using Python's logging module
'''

import logging

logging.basicConfig(
    filename='testPrg.log',
    level=logging.DEBUG, 
    format='%(asctime)s -> %(levelname)s -> %(message)s'
)

try:
    10 / 0.0
except ZeroDivisionError as e:
    logging.exception('Exception Occurred!')
