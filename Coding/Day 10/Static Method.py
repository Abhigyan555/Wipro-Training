'''
Name: Abhigyan Maji
ID: 30382
Date: 17 July 2025  
Purpose: Define a static method to check the strength of a password based on length, presence of uppercase letters, and digits
'''

class PasswordUtils:
    @staticmethod
    def isStrong(password):
        return (
            len(password) >= 8 and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password)
        )
       
if __name__ == '__main__':
    password = 'testone'
    print(f"password: {password} is {'Strong' if PasswordUtils.isStrong(password) else 'Weak'}")

    password = 'test1One#$'
    print(f"password: {password} is {'Strong' if PasswordUtils.isStrong(password) else 'Weak'}")
