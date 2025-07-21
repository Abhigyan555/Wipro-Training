'''
Name: Abhigyan Maji
ID: 30382
Date: 16 July 2025  
Purpose: Defines a class with number operation methods.
'''

class NumOps:
    def __init__(self, num):
        self.num = num

    def isEven(self):
        return self.num % 2 == 0

    def isPrime(self):
        if self.num <= 1:
            return False
        for i in range(2, int(self.num**0.5) + 1):
            if self.num % i == 0:
                return False
        return True

    def isArmstrong(self):
        digits = str(self.num)
        power = len(digits)
        total = sum(int(d)**power for d in digits)
        return total == self.num

if __name__ == '__main__':
    obj = NumOps(10)
    print(f'10 --> Even: {obj.isEven()}, Prime: {obj.isPrime()}, Armstrong: {obj.isArmstrong()}')

    obj1 = NumOps(153)
    print(f'153 --> Even: {obj1.isEven()}, Prime: {obj1.isPrime()}, Armstrong: {obj1.isArmstrong()}')

    obj2 = NumOps(101)
    print(f'101 --> Even: {obj2.isEven()}, Prime: {obj2.isPrime()}, Armstrong: {obj2.isArmstrong()}')
