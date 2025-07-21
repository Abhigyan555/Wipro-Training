'''
Name: Abhigyan Maji
ID: 30382
Date: 17 July 2025
Purpose: Create a Student class with an alternative constructor and a static method to check if grade is pass.
'''

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = int(age)
        self.grade = float(grade)

    @classmethod
    def from_string(cls, data):
       
        name, age, grade = data.split('|')
        return cls(name, age, grade)

    @staticmethod
    def is_pass(grade):
        return grade >= 50

# Example usage:
student1 = Student.from_string("Abhi|19|92")
print("Name:", student1.name)
print("Passed:", Student.is_pass(student1.grade))

student1 = Student.from_string("Jeet|19|82")
print("Name:", student1.name)
print("Passed:", Student.is_pass(student1.grade))

student1 = Student.from_string("Rana|19|62")
print("Name:", student1.name)
print("Passed:", Student.is_pass(student1.grade))
