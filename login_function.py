user_login = [
    'petrmara',
    'user_1'
]

user_password = [
    'password123',
    '54321'
]

login = ''
password = ''

def log_in(user_login, user_password):
    if login in username_login:
        if password in username_password:
            if uzivatele_login.index(login) == uzivatele_password.index(password): #check if the indexes in the given lists match
                print('You got in')
    else:
        print("Unfortunately, you don't have permission.")
        novy_user = input('To register your account, type "Yes": ').lower() #query to register a new user
        return novy_user

def add_user(login, password, user_login, user_password, new_user):
    if novy_user == 'yes':
        user_login.append(login)
        user_password.append(password)
        print('Your account has been successfully created :)')

def main():
    login = input('Enter your login credentials: ')
    password = input('Enter your password: ')
    new_user = log_in(user_login, user_password)
    add_user(login, password, user_login, user_password, new_user)
    print(username_login, username_password) #validate credit


if __name__ == "__main__":
    main()
