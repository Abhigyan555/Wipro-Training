'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 7 July 2025
    Purpose- Calender Problem
'''

w = 2
print('Su Mo Tu We Th Fr Sa')
for _ in range(w):
    print(f'{" ":>3}', end='')

for cnt in range(1,31):
    print(f'{cnt:>3}', end='')
    if (w + cnt) % 7 == 0:
        print()