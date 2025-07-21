import os

def getSize(path='test.txt'):
    size = os.path.getsize(path)
    print(f"Size of {path}: {size} bytes")

def getPermissions(path='test.txt'):
    permissions = oct(os.stat(path).st_mode)[-3:]
    print(f"Permissions of {path}: {permissions}")
