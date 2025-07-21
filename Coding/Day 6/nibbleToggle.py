"""
Name- Abhigyan Maji
ID- 30382
Date- 12 July 2025 
Purpose- Toggling a nibble
"""

def nibbleToggle(num, pos):  # pos = 0 for lower nibble, 1 for upper nibble
    if pos == 0:
        mask = 0x0F
    else:
        mask = 0xF0
    result = num ^ mask
    print("After nibble toggle:", result)


num = int(input("Enter a number: "))
pos = int(input("Enter nibble position (0 or 1): "))
nibbleToggle(num, pos)