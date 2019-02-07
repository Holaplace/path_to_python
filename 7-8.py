sandwich_orders = ['a','b','c']
finished_sandwiches = []

while sandwich_orders:
    print('I made')
    finished_sandwiche = sandwich_orders.pop()

    finished_sandwiches.append(finished_sandwiche)

for sand in sorted(finished_sandwiches):
    print(sand + ' is already finished.')