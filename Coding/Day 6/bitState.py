"""
Name- Abhigyan Maji
ID- 30382
Date- 12 July 2025 
Purpose- Checking the Bit State
"""

def bitState(num, pos):
    if (num & (1 << pos)) != 0:
        print("Bit is 1")
    else:
        print("Bit is 0")


num = int(input("Enter a number: "))
pos = int(input("Enter bit position: "))
bitState(num, pos)