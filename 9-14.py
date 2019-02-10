from random import randint


class Die:
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        x = randint(1, self.sides)
        #return x
        print('The lucky number is: ' + str(x))


six = Die()
for i in range(0, 10):
    six.roll_die()

