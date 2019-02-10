import json


def store_num():
    favorite_num = input("Please input you favorite number: ")
    filename = 'favorite_num.json'
    with open(filename, 'w') as f_obj:
        json.dump(favorite_num, f_obj)
        return favorite_num


def read_num():
    filename = 'favorite_num.json'
    try:
        with open(filename) as f_obj:
            favorite_num = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_num


def reply_num():
    favorite_num = store_num()
    if favorite_num:
        print('Your favorite number is: ' + favorite_num)
    else:
        favorite_num = read_num()
        print("I already know your favorite number is: " + favorite_num)


reply_num()
