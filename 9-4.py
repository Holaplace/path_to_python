class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.count = 10

    def describe_restaurant(self):
        print('The restaurant name is '
              + self.restaurant_name.title()
              + ', and the cuisine type is '
              + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is opening.')

    def number_served(self):
        print("This restaurant has " + str(self.count) + " people been here.")

    def set_number_served(self,num):
        self.count = num
        print("This restaurant has " + str(self.count) + " people been here.")

    def increment_number_served(self,num_increment):
        self.count += num_increment
        print("This restaurant has " + str(self.count) + " people (new) been here.")


res = Restaurant('me', 'chinese')
res.describe_restaurant()
res.increment_number_served(80)