'''
Name: Abhigyan Maji
ID: 30382
Date: 17 July 2025  
Purpose: Demonstrate logging to a file using DEBUG, INFO, and WARNING levels with timestamped formatting
'''

import logging

logging.basicConfig(
    filename='testPrg.log',
    level=logging.DEBUG, 
    format='%(asctime)s -> %(levelname)s -> %(message)s'
)

logging.debug('This is a debug level message')
logging.info('This is an info level message')
logging.warning('This is a warning level message')
