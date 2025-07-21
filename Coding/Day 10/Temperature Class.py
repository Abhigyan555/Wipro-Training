'''
Name: Abhigyan Maji
ID: 30382
Date: 17 July 2025
Purpose: Create a Temperature class with class methods to initialize from Celsius/Fahrenheit and static methods for conversion.
'''

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def fromCelsius(cls, celsius):
        return cls(celsius)

    @classmethod
    def fromFahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

# Example usage:
temp1 = Temperature.fromCelsius(25)
temp2 = Temperature.fromFahrenheit(98.6)

print("From Celsius: ", temp1.celsius, "°C")
print("From Fahrenheit: ", temp2.celsius, "°C")
print("25°C in Fahrenheit:", Temperature.celsius_to_fahrenheit(25))
print("98.6°F in Celsius:", Temperature.fahrenheit_to_celsius(98.6))
