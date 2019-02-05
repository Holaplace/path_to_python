name_list = ['Amy','Bob','Candy','Ellen']
print('I can only invite two person')

popped_1 = name_list.pop()
print(popped_1 + ', you can not be taken into.')
popped_2 = name_list.pop()
print(popped_2 + ', you can not be taken into.')

for each_name in name_list:
    print("I wanna invite " + each_name + " to take part in my party.")

del name_list[-1]
del name_list[-1]

print(name_list)