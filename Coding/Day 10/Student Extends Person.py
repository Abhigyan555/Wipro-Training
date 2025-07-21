'''
Name: Abhigyan Maji
ID: 30382
Date: 17 July 2025
Purpose: Create a Student class that inherits from Person class and adds a grade data member.
'''

# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Derived Class
class Student(Person):  # Inheriting from Person
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # Call the constructor of Person
        self.grade = grade  # Additional attribute

    def show_student_info(self):
        self.show_person_info()  # Call method from Person
        print(f"Grade: {self.grade}")

# Example usage
student1 = Student("Abhigyan", 21, 88)
student1.show_student_info()
