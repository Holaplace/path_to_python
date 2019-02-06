#names = ['admin','a','b','c','d']
names = []

if names:
    for name in names:
        if name == 'admin':
            print('Hello admin, would you like to see a status report?')
        elif name in names:
            print('Hello ' + name + ', thank you for logging in again.')
else:
    print('We need to find some users!')