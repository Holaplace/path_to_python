favorite_places = {
    'amy': {'city':'CA','city2':'BJ'},

    'bob': {'city':'HU','city2':'CA'},

    'candy': {'city':'RO','city2':'HU'},
    }

for name,place in favorite_places.items():
    print('\nName: ' + name.title())
    city = place['city'] + ',' + place['city2']
    print('City: ' + str(city))