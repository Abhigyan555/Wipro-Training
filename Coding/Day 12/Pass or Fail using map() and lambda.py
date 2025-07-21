'''
Name: Abhigyan Maji
ID: 30382
Date: 19 July 2025  
Purpose: Pass or Fail using map() and lambda
''' 
marks = [35, 42, 80, 25, 60]
check_pass = lambda mark: "Pass" if mark >= 40 else "Fail"
result = list(map(check_pass, marks))
print(result)
