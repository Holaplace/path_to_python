names = ['admin','a','b','c','d']

for name in names:
    if name == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello ' + name + ', thank you for logging in again.')