''' 
    Name: Abhigyan Maji
    ID:  30382
    Date: 4 July 2025
    Purpose: Program on Range of prices for a single item
'''

print("Checking price range for item: 'Notebook'")
price = float(input("Enter the price of the notebook: "))

min_price = 10.0
max_price = 100.0

if min_price <= price <= max_price:
    print("Price is within range.")
else:
    print("Price is out of range.")
