#TO DO: create a valid input function

def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).upper()
        if response == option1:
            return response
        elif response == option2:
            return response
        else: 
            print("Sorry, that is not a valid answer. Please try again and enter a valid input. Type either Y or N.")
            

acceptable_answers = ['Y', 'N', 'YES', 'NO']

def valid_input_list(prompt, list_name):
    while True:
        response = input(prompt).upper()
        if response in list_name:
            if response == 'YES' or response == 'Y':
                print("You know it!")
                break
            elif response == 'NO' or response == 'N':
                print("whaddya mean?")
                break
        else: 
            print("Sorry, that is not a valid answer. Please try again and enter a valid input. Type either Y or N.")
            
