prompt = '\nPlease tell me your age: '

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print('Free')
        elif age <12:
            print('$10')
        else:
            print('$15')