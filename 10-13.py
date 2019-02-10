import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_name():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username


def ask():
    """询问是否是新用户"""
    username = get_stored_username()
    print("Is this your username? " + username)
    answer = input("If right, please input y; else, please input n: \n")
    if answer == 'y':
        greet_old_user()
    else:
        greet_new_user()


def greet_old_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    print("Welcome back, " + username + "!")


def greet_new_user():
    username = get_new_name()
    print("We'll remember you when you come back, " + username + "!")


ask()
