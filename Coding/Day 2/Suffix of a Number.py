'''
   
    Name: Abhigyan Maji
    ID:  30382
    Date: 4 July 2025
    Purpose: Suffix Of a Number
 
'''
num = int(input("Enter a number: "))


last_two = num % 100
last_digit = num % 10


suffix = (last_two in [11, 12, 13] and 'th') or \
         (last_digit == 1 and 'st') or \
         (last_digit == 2 and 'nd') or \
         (last_digit == 3 and 'rd') or \
         'th'

print(str(num) + suffix)
