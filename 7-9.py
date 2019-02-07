sandwich_orders = ['a','pastrami','b','pastrami','c','pastrami']
print('Pastrami is ready sold out.')

active = True
while active:
    sandwich_orders.remove('pastrami')
    if 'pastrami' not in sandwich_orders:
        break

for sand in sorted(sandwich_orders):
    print(sand)