'''
Name: Abhigyan Maji
ID: 30382
Date: 16 July 2025  
Purpose: Perform bitwise operations like checking bit state, toggling a bit, and toggling the lower nibble of a number
'''

class BitOps:
    def __init__(self, num, pos):
        self.num = num
        self.pos = pos

    def __str__(self):
        return f'Number: {self.num}, Binary: {bin(self.num)}'

    def bitState(self):
        mask = 1 << self.pos
        return 1 if (self.num & mask) else 0

    def bitToggle(self):
        mask = 1 << self.pos
        self.num ^= mask
        return self.num

    def nibbleToggle(self):
        mask = 0xF
        self.num ^= mask
        return self.num

if __name__ == '__main__':
    b = BitOps(10, 1)
    print(b)
    print("Bit State at position 1:", b.bitState())
    print("After Bit Toggle at position 1:", b.bitToggle())
    print("After Nibble Toggle (lower 4 bits):", b.nibbleToggle())
