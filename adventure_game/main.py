import time 
import random 


random_creatures = ["gorgon", "vampire", "gruffalo", "zombie", "minatour"]
items = ["lollipop", "rock"]

def print_pause(string):
    '''
    function that pauses after
    printing a given string
    '''
    print(string)
    time.sleep(2)


def greet_user(username):
    print_pause("Hello, " + username + "!")

def item_pickup():
    print_pause("You see a faint glimmer in the sunshine")
    print_pause("You notice that it is in fact a sword")
    choice = input("Do you want to pick up the sword? Y/N ")
    if choice == "Y":
        items.append("sword")
        inventory = ', '.join(items)
        print_pause(f"You're inventory now contains {len(items)} items. You have: \n {inventory}")
    else: 
        print_pause("Are you sure?")


def witch_house():
    #TO DO: Joe add more exploration to the story and then add this function to the first_choice()
    return 


def first_choice():
    '''
    function that asks for
    users input & returns different outcomes depending on the scenario
    '''
    choice = input("Do you to exit the cave? Type Y/N \n")
    if choice == "Y":
        print_pause("You find yourself in a field of flowers")
        item_pickup()
        #TO DO: Add more exploration to the story. - Joe
    else: 
        print_pause('''Stumbling around the cave, you hear an ominous noise coming from deep in the darness \n ''')
        creature  = random.choice(random_creatures)
        print_pause(f"Oh no! You encounter a {creature}")
        #TO DO: new function that gives a choice to fight the monster or not - Ellen 
        #TO DO: function should first show XP points of the monster & inventory before presenting choice. - Ellen 


def intro(): 
    
    greet_user('Arcade') #calling the function
    greet_user('Ellen')
    greet_user('Sophie')
    greet_user('Joe')
    string_items = ', '.join(items)
    print_pause("You find yourself in a dark cave and you only have a " + string_items + " in your hand")
    first_choice()


intro()

 
#creating a print pause function to make it more dramatic. in the terminal
# Any other project ideas? 