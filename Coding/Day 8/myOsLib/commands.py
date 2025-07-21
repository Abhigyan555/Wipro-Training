import os
import datetime

def listDir(path='.'):
    print(f"Contents of '{path}':", os.listdir(path))

def getCWD():
    print("Current Working Directory:", os.getcwd())

def date():
    print("Today's Date:", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
