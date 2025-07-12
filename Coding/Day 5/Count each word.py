string = '''Checking some strings here
this is to test here
The idea here is to keep count of each word'''
dt = {}
for each in string.split():
    if each not in dt:
        dt.setdefault(each, 1)
    else:
        dt[each] += 1

print(dt)