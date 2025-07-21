import shutil
import os

def copy(src='test.txt', dest='test_copy.txt'):
    shutil.copy(src, dest)
    print(f"Copied from {src} to {dest}")

def move(src='test_copy.txt', dest='moved_test.txt'):
    shutil.move(src, dest)
    print(f"Moved from {src} to {dest}")

def remove(path='moved_test.txt'):
    os.remove(path)
    print(f"Removed file: {path}")
