my_pizza = ['A','B','C']
friens_pizza = my_pizza[:]

my_pizza.append('D')
friens_pizza.append('E')

for my_name in my_pizza:
    print(my_name)

print('\n')

for friens_name in friens_pizza:
    print(friens_name)