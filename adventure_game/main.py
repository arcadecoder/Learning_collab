import time 
import random 


random_creatures = ["gorgon", "vampire", "gruffalo", "zombie", "minatour"]
items = ["lollipop"]

def print_pause(string):
    '''
    function that pauses after
    printing a given string
    '''
    print(string)
    time.sleep(2)


def greet_user(username):
    print_pause("Hello, " + username + "!")


def first_choice():
    '''
    function that asks for
    users input & returns different outcomes depending on the scenario
    '''
    choice = input("Do you to exit the cave? Type Y/N \n")
    if choice == "Y":
        print_pause("You find yourself in a field of flowers")
    else: 
        print_pause('''Stumbling around the cave, you hear an ominous noise coming from deep in the darness \n ''')
        creature  = random.choice(random_creatures)
        print_pause(f"Oh no! You encounter a {creature}")


def intro(): 
    
    greet_user('Arcade') #calling the function
    greet_user('Ellen')
    greet_user('Sophie')
    greet_user('Joe')
    # TO DO: Ellen - figure out how to print items as a string without []
    print(type(items))
    print_pause(f"You find yourself in a dark cave and you only have a {items} in your hand")
    first_choice()


intro()

 
#creating a print pause function to make it more dramatic. in the terminal
# Any other project ideas? 