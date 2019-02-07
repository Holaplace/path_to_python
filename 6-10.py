files = {
    'amy':{'num_1':5, 'num_2':2},
    'bob':{'num_1':6, 'num_2':8},
    'candy':{'num_1':9, 'num_2':6},
    'doby':{'num_1':1, 'num_2':5},
    'john':{'num_1':7, 'num_2':1},
    }

for name,num in files.items():
    print('\nName: ' + name)
    favo_num = num['num_1'] + num['num_2']
    print("Number is " + str(favo_num) + '.')