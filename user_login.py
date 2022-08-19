
class UserLogin:

    def __init__(self, login:str, password:str):
        self.login = login
        self.password = password
        self.user_login = [
            'petrmara',
            'user_1'
        ]
        self.user_password = [
            'password123',
            '54321'
        ]


    def log_in(self):
        if self.login in self.user_login:
            if self.password in self.user_password:
                if self.user_login.index(self.login) == self.user_password.index(self.password): #check if the indexes in the given lists match
                    print('You got in')
        else:
            print("Unfortunately, you don't have permission.")
            new_user = input('To register your account, type "Yes": ').lower() #query to register a new user
            return new_user

    def add_user(self, new_user):
        if new_user == 'yes':
            self.user_login.append(self.login)
            self.user_password.append(self.password)
            print('Your account has been successfully created :)')

def main():
    login = input('Enter your login credentials: ')
    password = input('Enter your password: ')
    login = UserLogin(login, password)
    new_user = login.log_in()
    login.add_user(new_user)
    print(login.user_login, login.user_password) #validate credit


if __name__ == "__main__":
    main()
