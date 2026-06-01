from app.database import create_user, delete_user, create_database, get_user_by_username
from app.security import authenticate_user, hash_password
from app.transactions import transfer

import sys
"""A simple CLI
Give the user basic choices to interact with their account
"""

def main_menu(username):
    while True:
        choice = input("Enter \n1. If you would like to inspect your balance. \n2. If you would like to make a transfer. \n3. If you would like to delete your account. \n4. Quit. \n>")
        if choice == "1":
            user = get_user_by_username(username)
            print(f"Balance: {user["balance"]}")

        elif choice == "2":
            username2 = input("Enter the account you want to transfer funds to: ")

            try:
                amount = int(input("Enter the quantity of the funds you wish to transfer: "))

            except ValueError:
                print("Incorrect amount value entered")
                continue

            user_reciver = get_user_by_username(username2)
            if user_reciver is None:
                print("Incorrect username of reciver entered")
                continue

            successful_transfer = transfer(username, username2, amount)
            if successful_transfer:
                print("Transfer was successful")
            
            else:
                print("Something went wrong. Please check you balance, and ensure you are entering a valid fund quantity for transfer.")

        elif choice == "3":
            auth = authenticate_user(username, input("Enter your password: "))
            if auth is False:
                print("Passwords is incorrect")
            else:
                confirm = input("Are you sure you want to delete your account? \nThis action is ireversable. \nEnter 'YES' to delete your account. \n> ")
                if confirm == "YES":
                    delete_user(username)
                    print("Account was deleted")
                    sys.exit()

        elif choice == "4":
            sys.exit()


def main():
    print("App start")
    create_database()

    while True:
        choice = input("Enter \n1. If you have an existing account. \n2. If you would like to make a new account. \n3. Quit. \n>")
        if choice == "1":
            username = input("Enter your username: ")
            

            auth = authenticate_user(username, input("Enter your password: "))

            user = get_user_by_username(username)
            if user is None:
                print("Username or Password is incorrect")
                break

            if auth is False:
                print("Username or Password is incorrect")
                break

            main_menu(username)

        elif choice == "2":
            username = input("Enter your username: ")

            password = input("Password: ")
            confirm = input("Confirm Password: ")

            if password != confirm:
                print("Passwords do not match")
                break

            create_user(username, hash_password(password))

            print("Account created")
            main_menu(username)

        elif choice == "3":
            sys.exit()

if __name__ == "__main__":
    main()