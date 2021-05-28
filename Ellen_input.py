#TO DO: create a valid input function

def valid_input():
    while True:
        response = input('Is Arcade the best programmer ever!? Type Y or N. \n')
        if response.lower() not in ('y', 'n', 'yes', 'no'):
            print('Sorry, that is not a valid answer. Please try again and enter a valid input. Type either Y or N. \n')
        else:
            break

valid_input()