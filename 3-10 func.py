name_list = ['Amy','Bob','Candy','Ellen']

for each_name in name_list:
    print(each_name)

for each_name in name_list:
    print("Hi, " + each_name)

print('I would like to own a ' + name_list[1] +'.')

for each_name in name_list:
    print("I wanna invite " + each_name + " to take part in my party.")

popped_name = name_list.pop(3)
print(popped_name +" cannot take into this party.")
name_list.append('Tim')

for each_name in name_list:
    print("I wanna invite " + each_name + " to take part in my party.")