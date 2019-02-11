def get_formatted_name(city, country, population=''):
    """Generate a neatly formatted full name."""
    if population:
        full_name = city + ' ' + country + ' ' + population
    else:
        full_name = city + ' ' + country
    return full_name.title()