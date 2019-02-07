not_will = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

will = ['phil', 'amy']

for name in not_will.keys():
    if name in will:
        print(str(name.title()) + ', thank you.')
    else:
        print(str(name.title()) + ', please take the poll.')