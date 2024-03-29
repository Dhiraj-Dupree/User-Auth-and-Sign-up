def activeUserLogin(username, password, takenUsers):
    login = input("Enter your username to log in: ")

    if login not in takenUsers:
        print("User not found. Are you sure you're logging in with the correct username?")
    else:
        entered_password = input("Enter your password: ")
        if entered_password == password.get(login):
            print("Login successful!")
        else:
            print("Incorrect password")

# Usage example
takenUsers = ['User123456', 'UserAbcdefg', 'User654321']
username = takenUsers
passwords = {'User123456': 'mypassword123', 'UserAbcdefg': 'abcpassword', 'User654321': '654password'}
activeUserLogin(username, passwords, takenUsers)


