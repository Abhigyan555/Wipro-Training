'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 7 July 2025
    Purpose- Printing Cash Memo     	
'''

lst = [
    ['Dairy Milk', 45.0],
    ['Kit Kat', 30.5],
    ['Perk', 10.0],
    ['Cadbury Celebrations', 120.0],
    ['Snickers', 35.0]
]

quantity = [4, 2, 6, 5, 3]

print(' %s' % ('-' * 55))
print(f'| %-5s|%-22s|%-4s|%-6s|%-10s|' % ('SlNo', 'Name', 'Qty', 'Price', 'Amount'))
print(' %s' % ('-' * 55))

total = 0.0
for i in range(len(quantity)):
    price = lst[i][1]
    qty = quantity[i]
    amount = qty * price
    total += amount
    print(f'| {i+1:^5}|{lst[i][0]:<22}|{qty:^4}|{price:<6.2f}|{amount:10.2f}|')

print(' %s' % ('-' * 55))
print(f'| %42s%10.2f|' % ('| Total|', total))
print(' %s' % ('-' * 55))
