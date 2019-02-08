def show_magicians(names):
    for name in names:
        print(name)


unprinted_name = ['a','b','c','d']
printed_name = []

def make_great(nami):
    while nami:
        ing = nami.pop()
        printed_name.append(ing)
    nanos = sorted(printed_name)
    for nano in nanos:
        print(nano + ', the Great!')

show_magicians(unprinted_name)
make_great(unprinted_name)