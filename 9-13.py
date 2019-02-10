from collections import OrderedDict

file = OrderedDict()

file['amy'] = 5
file['bob'] = 8
file['candy'] = 6
file['doby'] = 9
file['john'] = 0


for name, num in file.items():
    print(str(name.title()) + "'s number is " + str(num) +'.')