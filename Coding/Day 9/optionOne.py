'''
Name: Abhigyan Maji
ID: 30382
Date: 16 July 2025  
Purpose: Create a command-line utility to list files, display today's date, and echo a given string using argparse
'''

import argparse
import os
import datetime

parser = argparse.ArgumentParser(description="Command line options: list files, show date, echo message")

parser.add_argument('-1', '--list', action='store_true', help="List all files and directories")
parser.add_argument('-d', '--date', action='store_true', help="Display today's date")
parser.add_argument('-e', '--echo', type=str, help="Display the given string")

args = parser.parse_args()

if args.list:
    os.system('dir')  # Use 'ls' if you're on Unix/Linux/Mac

if args.date:
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    print("Today's date is:", today)

if args.echo:
    print("Echoed string:", args.echo)
