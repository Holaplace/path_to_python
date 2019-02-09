class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts =0

    def describe_user(self):
        print('User_name: '
              + self.first_name.title()
              + ' '
              + self.last_name.title())

    def greet_user(self):
        print('Hello, '
              + self.first_name.title()
              + ' '
              + self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1
        print('New number is: ' + str(self.login_attempts))

    def reset_login_attempts(self):
        self.login_attempts = 0
        print('Set login number is: ' + str(self.login_attempts))

user = User('eliot','xu')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

user.reset_login_attempts()

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()