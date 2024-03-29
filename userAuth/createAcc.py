#user site
#create a profile also sign in method
#ask the length of the password
#check if the password is valid (that its not used)
import random
import string
class newuser:
      import string
import random

class newuser:
    @staticmethod
    def CreateProfile():
        takenUsers = ['User123456', 'UserAbcdefg', 'User654321']
        CreateOrLogin = input("Welcome, create an account with us enter 'create'!: ")

        while not (CreateOrLogin.lower() == 'create'):
            print("Invalid input, please enter 'create'!")
            CreateOrLogin = input("Welcome, create an account with us!: ")

        if CreateOrLogin == 'create':
            username = input("Enter a username for your new account: ")
            while any(char in string.punctuation for char in username):
                print("Invalid username! Please use numbers and letters.")
                username = input("Enter a username for your new account: ")

            while len(username) < 8:
                print("Username must be at least 8 characters long.")
                username = input("Enter a username for your new account: ")

            while username in takenUsers:
                print("Username is already taken. Please enter a different username.")
                username = input("Enter a username for your new account: ")

            takenUsers.append(username)
            print(f"Welcome {username}!")
            return username

    @staticmethod
    def newUserPassword(username):
        usersPW = {'User123456' : 'mypassword123', 'UserAbcdefg' : 'abcpassword', 'User654321' : '654password'}

        genPw = input(f"Alright, {username} time to create a password. Would you like one to be generated? (yes / no): ")

        if genPw.lower() == "yes":
            def generate(length=8):
                characters = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(random.choice(characters) for i in range(length))
                return password
            password = generate()
            print(f"Generated Password: {password}")
        elif genPw.lower() == "no":
            password = input("Enter your password: ")

        while len(password) < 8:
            print("Password must be at least 8 characters long.")
            password = input("Enter a password for your new account: ")

        while password in usersPW.values():
            print("Password is invalid. Please choose a different password.")
            password = input("Enter a password for your new account: ")

        usersPW[username] = password
        print(f"Password set for {username}")
        return password

# Usage example
takenUsers = ['User123456', 'UserAbcdefg', 'User654321']
username = newuser.CreateProfile()
password = newuser.newUserPassword(username)
# activeUserLogin(username, password, 'login', takenUsers)  # You need to implement activeUserLogin in the class as well


 
      
      

      








            
            
            
            
            
            
            
            
            
            
            








#password = generate(12)
#print(f"generated password: {password}")


