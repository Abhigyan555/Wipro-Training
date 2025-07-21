"""
Name- Abhigyan Maji
ID- 30382
Date- 12 July 2025 
Purpose- Rotating bits
"""

def rightRotate(num, nbits):
    result = ((num >> nbits) | (num << (8 - nbits))) & 0xFF
    print("After right rotate:", result)


num = int(input("Enter a number: "))
nbits = int(input("Enter number of bits to rotate: "))
rightRotate(num, nbits)