file_1 = {'first_name':'amy',
        'last_name':'green',
        'age':'22',
        'city':'CA'}

file_2 = {'first_name':'bob',
        'last_name':'underwood',
        'age':'25',
        'city':'HU'}

file_3 = {'first_name':'candy',
        'last_name':'xu',
        'age':'15',
        'city':'RO'}

file = [file_1,file_2,file_3]
for name in file:
    print('Name: ' + name['first_name'].title() + ' ' +name['last_name'].title())
    print('Age: ' + name['age'].title())
    print('City: ' + name['city'] + '\n')