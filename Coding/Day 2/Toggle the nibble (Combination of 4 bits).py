''' 
    Name: Abhigyan Maji
    ID:  30382
    Date: 4 July 2025
    Purpose: Toggle the nibble (Combination of 4 bits)
'''
num, pos=10,2
npos=pos // 4*4
res= num ^ 0xf << npos
print (f'After toggling {npos} nibble number on {num} is {res}')
