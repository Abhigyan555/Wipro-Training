"""
Name- Abhigyan Maji
ID- 30382
Date- 12 July 2025 
Purpose- Toggle a Bit
"""

def bitToggle(num, pos):
    result = num ^ (1 << pos)
    print("Result after toggling:", result)


num = int(input("Enter a number: "))
pos = int(input("Enter bit position: "))
bitToggle(num, pos)