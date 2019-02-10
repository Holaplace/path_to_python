class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        # for privilege in self.privileges:
        #     print('Admin own these privileges: ' + privilege)
        print(self.privileges)


class Admin:
    def __init__(self):
        self.privileges = Privileges()