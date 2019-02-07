prompt = '\nPlease tell me your age: '

while True:
    age = int(input(prompt))
    if age < 3:
        print('Free')
    elif age <12:
        print('$10')
    else:
        print('$15')