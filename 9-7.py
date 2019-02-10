class User:
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

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        # for privilege in self.privileges:
        #     print('Admin own these privileges: ' + privilege)
        print(self.privileges)


user = Admin('eliot', 'xu')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

user.reset_login_attempts()

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

user.show_privileges()