import json


def get_stored_user_name():
    """"Get stored username if available"""
    filename = 'Test_15_greeting_user.json'
    try:
        with open(filename) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """Greet the user by the name"""
    username = get_stored_user_name()
    if username:
        print("Welcome back, " + username + '!')
    else:
        username = input('Whats your name? ')
        filename = 'Test_15_greeting_user.json'
        with open(filename, 'w') as file:
            json.dump(username, file)
            print("We`ll remember you when you come back, " + username + '!')


greet_user()
