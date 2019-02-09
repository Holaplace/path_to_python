class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('The restaurant name is '
              + self.restaurant_name.title()
              + ', and the cuisine type is '
              + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is opening.')

res = Restaurant('me', 'chinese')
res.describe_restaurant()

res1 = Restaurant('you','US')
res1.describe_restaurant()

res2 = Restaurant('she', 'CA')
res2.describe_restaurant()