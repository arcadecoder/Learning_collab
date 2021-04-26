import time 
import random 


random_creatures = ["gorgon", "vampire", "gruffalo", "zombie", "minatour"]


def intro():

    def greet_user(username):
        print("Hello, " + username + "!")
    
    greet_user('Arcade')
    greet_user('Ellen')
    greet_user('Sophie')

    print('''
    You find yourself in a dark cave 
    You only have a lollipop in your hand
    ''')
    
    choice = input("Do you to exit the cave? Type Y/N \n")

    if choice == "Y":
        print("You find yourself in a field of flowers")
    else: 
        print('''Stumbling around the cave, you hear an ominous noise coming from deep in the darness \n ''')
        creature  = random.choice(random_creatures)
        print(f"Oh no! You encounter a {creature}")

intro()


#TO DO: Wrap the introduction in  a function - Ellen
#TO DO: create a second part of the introduction that occurs when you type Yes - Sophie