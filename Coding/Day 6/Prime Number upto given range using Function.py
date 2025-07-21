'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 12 July 2025
    Purpose- Prime or not upto a range using funtion
'''

def printprime(n1,n2):
    for i in range(n1,n2+1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            print(i,end="\t")

n1=int(input("Enter Lower Limit: "))
n2=int(input("Enter Upper Limit: "))
printprime(n1,n2)
