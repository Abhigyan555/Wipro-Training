'''
Name: Abhigyan Maji
ID: 30382
Date: 19 July 2025  
Purpose:  Access Control
''' 
def requireAdmin(func):
    def wrapper(user, *args, **kwargs):
        if user.get('role') == 'admin':
            return func(user, *args, **kwargs)
        else:
            print("Access Denied")
    return wrapper

@requireAdmin
def deleteUser(user, userId):
    print(f"User {userId} deleted by {user['username']}")

user1 = {'username': 'Abhigyan Maji', 'role': 'admin'}
user2 = {'username': 'Jeet Maji', 'role': 'user'}

deleteUser(user1, 100)  # Allowed
deleteUser(user2, 200)  # Access Denied
