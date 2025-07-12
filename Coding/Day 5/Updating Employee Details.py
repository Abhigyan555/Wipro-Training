employee = {
    "name": "Abhigyan",
    "position": "Manager",
    "salary": 75000
}

# a) Print position
print("Position:", employee["position"])

# b) Increase salary by 10%
increase = employee["salary"] * 10 / 100   # Calculate 10% increase
employee["salary"] = employee["salary"] + increase  # Add increase to old salary

print("Updated Salary:", employee["salary"])

# c) Add new key
employee["department"] = "Training"

# Show full updated dictionary
print("Updated Employee:", employee)
