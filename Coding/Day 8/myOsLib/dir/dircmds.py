import os

def makeDir(path='new_folder'):
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")

def rmDir(path='new_folder'):
    os.rmdir(path)
    print(f"Directory removed: {path}")

def chDir(path='.'):
    os.chdir(path)
    print(f"Changed directory to: {path}")
