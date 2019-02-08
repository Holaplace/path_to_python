def make_car(zhizao, xinghao, **other):
    profile = {}
    profile['zzs'] = zhizao
    profile['xh'] = xinghao
    for key, value in other.items():
        profile[key] = value
    return profile

car_profile = make_car('subaru', 'outback',
                            color='blue',
                            tow_package=True)
print(car_profile)