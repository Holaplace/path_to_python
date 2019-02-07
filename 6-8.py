files = {
    'amy': {'age':'22',
            'city':'CA'},

    'bob': {'age':'25',
            'city':'HU'},

    'candy': {'age':'15',
            'city':'RO'},
    }

for name,file in files.items():
    print('\nName: ' + name.title())
    print('Age: ' + file['age'])
    print('City: ' + file['city'])