"""
Name- Abhigyan Maji
ID- 30382
Date- 12 July 2025
Purpose- Keyword Arguments
"""
def funOne(a=1000, b=2000, *args, **kwargs):
    print(f'args a: {a}  b: {b}  args:  {args}  kwargs: {kwargs}')
    print('*' * 40)
 
if __name__ == '__main__':
    funOne(num=10, name='Abhigyan Maji')
    funOne(10,20,30,40,50, num=10, name='Abhigyan Maji')
    funOne(10,20,30)    
    funOne(10,20,30,40,50,60,70)
    funOne(10, 'Hello How', 123.345)
    funOne((10, 'Hello How', 123.345), 20, 30)