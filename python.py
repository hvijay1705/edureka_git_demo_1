import datetime
import random

def greet_user(name):
    now = datetime.datetime.now()
    number = random.randint(1, 100)
    print(f"Hello, {name}! Welcome to Git Demo. Your ID number is: {number} and your login time in : {now}")

def main():
    
    user_name = input("Enter your first & last name: ")
    greet_user(user_name)

if __name__ == "__main__":
    main()
