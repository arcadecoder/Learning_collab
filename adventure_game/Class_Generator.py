import time
import random 

def print_pause(string):
    '''
    function that pauses after
    printing a given string
    '''
    print(string)
    time.sleep(2)

acceptable_answers_YN = ['Y', 'N', 'YES', 'NO'] 
acceptable_answers_A= ['A','a']
acceptable_answers_B= ['B','b']
acceptable_answers_C= ['C','c']
## creates a list of acceptable answers for each option

def valid_ABC_list(prompt, list_name):
    while True:
        response = input(prompt).upper()
        if response in list_name:
            if response in acceptable_answers_A:
                print('you have chosen A')
            elif response in acceptable_answers_B:
                print('You have chosen B')
            elif response in acceptable_answers_C:
                print('You have chosen C')
        else:
            print('Sorry what was that? Please type either A, B or C')
    
         


def intro():
    print_pause('Hello World!')
    print_pause('Shall we figure out what DND character you should play as')
    
def First_choice():
    print_pause ('Do you want to cast magic or smash things?')
    print_pause('Option A = Cast Magic')
    print_pause('Option B = Can I do Both?')
    print_pause('Option C = Me Smash')
    choice = input('A,B,C ?  \n')
    if choice in valid_ABC_list=='A':
        print_pause('Are you religious?')
        print_pause('Option A = Would you like to hear about my god')
        print_pause('Option B = No, not really')
        religious_Q = input('A or B \n')
        if religious_Q in acceptable_answers_A:
            print_pause('You should play as a Cleric')
        elif religious_Q in acceptable_answers_B:
            print_pause('Do you like to study?')
            print_pause('Option A = No, Studying is for losers')
            print_pause('Option B = Yes, I love learning')
            Study_Q = input('A or B? \n')
            if Study_Q in acceptable_answers_A:
                print_pause('Would you like your chacter to born with magic?')
                print_pause('Option A = Not Exactly')
                print_pause('Option B = Yes it is in thier blood')
                Born_this_way_Q = input('A or B?\n')
                if Born_this_way_Q in acceptable_answers_A:
                    print_pause('You should play as a warlock')
                    return
                elif Born_this_way_Q in acceptable_answers_B:
                    print_pause('You should play as a Sorerer')
                else:
                    print_pause('Fine be that way, have a nice day')
                    return
            elif Study_Q in acceptable_answers_B:
                print_pause('Would you like your character to be musically gifted?')
                print_pause('Option A = Not really')
                print_pause('Yes! they write poetry too')
                music_Q = input('A or B \n')
                if music_Q in acceptable_answers_A:
                    print_pause('Do you like animals ?')
                    print_pause('Option A = I prefer magic creatures')
                    print_pause('Option B = I actually prefer animals to people')
                    animals_Q=input('A or B? \n')
                    if animals_Q in acceptable_answers_A:
                        print_pause('You should play as a wizard')
                    elif animals_Q in acceptable_answers_B:
                        print_pause('You should play as a druid')
                    else:
                        return
                elif music_Q in acceptable_answers_B:
                    print_pause('Great, you should play as a bard')
                else:
                    print_pause('Fine be that way, have a nice day')
                    return
            else:
                print_pause('Fine be that way, have a nice day')
                return
        else:
            print_pause('Fine be that way, have a nice day')
            return
    elif choice in acceptable_answers_B:
        print_pause('Sure! Are you good with People') 
        print_pause('Option A = No, not really')
        print_pause('Option B = Yes ! People usually like me')
        Extroverty_Q=input('A or B? \n')
        if Extroverty_Q in acceptable_answers_A:
            print_pause('Do you like animals?')
            print_pause('Option A = They are so fluffy!')
            print_pause('Option B = Eh, they are ok')
            Animal_Q2=input('A or B? \n')
            if Animal_Q2 in acceptable_answers_A:
                print_pause('Except when they are not, you know')
                print_pause('Anyway you should play as a druid')
                return
            elif Animal_Q2 in acceptable_answers_B:
                print_pause('Are you sneaky?')
                print_pause('Option A = Not so much')
                print_pause('Option B = I am the night!')
                sneaky_Q=input('A or B?\n')
                if sneaky_Q in acceptable_answers_A:
                    print_pause('Do you prefer spells over melee?')
                    print_pause('Option A = Yeah melee is for losers')
                    print_pause('Option B = No, Spells are a bonus')
                    Bard_Q=input('A or B\n')
                    if Bard_Q in acceptable_answers_A:
                        print_pause('You should play as a Bard')
                    elif Bard_Q in acceptable_answers_B:
                        print_pause('Do you want to be wealthy?')
                        print_pause('Option A = Is that a question?!')
                        print_pause('Option B = Meh')
                        Money_Money=input('A or B? \n')
                        if Money_Money in acceptable_answers_A:
                            print_pause('You should play as a Rogue')
                        elif Money_Money in acceptable_answers_B:
                            print_pause('Do you know martial arts?')
                            print_pause('Option A = Nope')
                            print_pause('Option B = My fists hunger for Justice')
                            KungFu = input('A or B? \n')
                            if KungFu in acceptable_answers_A:
                                print_pause('You should play as a paladin')
                            elif KungFu in acceptable_answers_B:
                                print_pause('You should play as a Monk')
                            else:
                                print_pause('Fine be that way, have a nice day')
                                return
                        else:
                            print_pause('Fine be that way, have a nice day')
                            return
                    else:
                        print_pause('Fine be that way, have a nice day')
                        return
                elif sneaky_Q in acceptable_answers_B:
                    print_pause('You should play as a Rogue')
            else:
                print_pause('Fine be that way, have a nice day')
                return
        elif Extroverty_Q in acceptable_answers_B:
            print_pause('Are you sneaky?')
            print_pause('Option A = Not so much')
            print_pause('Option B = I am the night!')
            sneaky_Q=input('A or B?\n')
            if sneaky_Q in acceptable_answers_A:
                print_pause('Do you prefer spells over melee?')
                print_pause('Option A = Yeah melee is for losers')
                print_pause('Option B = No, Spells are a bonus')
                Bard_Q=input('A or B\n')
                if Bard_Q in acceptable_answers_A:
                    print_pause('You should play as a Bard')
                elif Bard_Q in acceptable_answers_B:
                    print_pause('Do you want to be wealthy?')
                    print_pause('Option A = Is that a question?!')
                    print_pause('Option B = Meh')
                    Money_Money=input('A or B? \n')
                    if Money_Money in acceptable_answers_A:
                        print_pause('You should play as a Rogue')
                    elif Money_Money in acceptable_answers_B:
                        print_pause('Do you know martial arts?')
                        print_pause('Option A = Nope')
                        print_pause('Option B = My fists hunger for Justice')
                        KungFu = input('A or B? \n')
                        if KungFu in acceptable_answers_A:
                            print_pause('You should play as a paladin')
                        elif KungFu in acceptable_answers_B:
                            print_pause('You should play as a Monk')
                        else:
                            print_pause('Fine be that way, have a nice day')
                            return
                    else:
                        print_pause('Fine be that way, have a nice day')
                        return
                else:
                    return
            elif sneaky_Q in acceptable_answers_B:
                print_pause('You should play as a Rogue')
            else:
                print_pause('Fine be that way, have a nice day')
                return
        else:
            print_pause('Fine be that way, have a nice day')
            return
    elif choice in acceptable_answers_C:
        print_pause('Ranged or Melee?')
        print_pause('Option A = Ranged')
        print_pause('Option B = Melee')
        Melee = input('A or B? \n')
        if Melee in acceptable_answers_A:
            print_pause('So are you good with People?')
            print_pause('Option A = Yes People Usually like me')
            print_pause('Option B = No, I prefer Animals')
            People_Person=input('A or B? \n')
            if People_Person in acceptable_answers_A:
                print_pause('Are you sneaky?')
                print_pause('Option A = Not so much')
                print_pause('Option B = I am the night!')
                sneaky_Q=input('A or B?\n')
                if sneaky_Q in acceptable_answers_A:
                    print_pause('Do you prefer spells over melee?')
                    print_pause('Option A = Yeah melee is for losers')
                    print_pause('Option B = No, Spells are a bonus')
                    Bard_Q=input('A or B\n')
                    if Bard_Q in acceptable_answers_A:
                        print_pause('You should play as a Bard')
                    elif Bard_Q in acceptable_answers_B:
                        print_pause('Do you want to be wealthy?')
                        print_pause('Option A = Is that a question?!')
                        print_pause('Option B = Meh')
                        Money_Money=input('A or B? \n')
                        if Money_Money in acceptable_answers_A:
                            print_pause('You should play as a Rogue')
                        elif Money_Money in acceptable_answers_B:
                            print_pause('Do you know martial arts?')
                            print_pause('Option A = Nope')
                            print_pause('Option B = My fists hunger for Justice')
                            KungFu = input('A or B? \n')
                            if KungFu in acceptable_answers_A:
                                print_pause('You should play as a paladin')
                            elif KungFu in acceptable_answers_B:
                                print_pause('You should play as a Monk')
                            else:
                                print_pause('Fine be that way, have a nice day')
                                return
                        else:
                            print_pause('Fine be that way, have a nice day')
                            return
                    else:
                        print_pause('Fine be that way, have a nice day')
                        return
                elif sneaky_Q in acceptable_answers_B:
                    print_pause('You should play as a Rogue')
                else:
                    print_pause('Fine be that way, have a nice day')
                    return
            elif People_Person in acceptable_answers_B:
                print_pause('You should play as a ranger')
                return
            else:
                print_pause('Fine be that way, have a nice day')
                return
        elif Melee in acceptable_answers_B:
            print_pause('Do you fight for a cause?')
            print_pause('Option A = Yes my beliefs define me')
            print_pause('Option B = Is money a cause?')
            Why_Fight=input('A or B? \n')
            if Why_Fight in acceptable_answers_A:
                print_pause('Do you know martial arts?')
                print_pause('Option A = Nope')
                print_pause('Option B = My fists hunger for Justice')
                KungFu = input('A or B? \n')
                if KungFu in acceptable_answers_A:
                    print_pause('You should play as a paladin')
                elif KungFu in acceptable_answers_B:
                    print_pause('You should play as a Monk')
                else:
                    print_pause('Fine be that way, have a nice day')
                    return
            elif Why_Fight in acceptable_answers_B:
                print_pause('Are you civilized')
                print_pause('Option A = I mean I dont eat people or anything...')
                print_pause('Option B = No, I was raised in the wilds')
                civilisation = input('A or B? \n')
                if civilisation in acceptable_answers_A:
                    print_pause('well that is a relief')
                    print_pause('You should play as a fighter')
                elif civilisation in acceptable_answers_B:
                    print_pause('You should play as a Barbarian')
                else:
                    print_pause('Fine be that way, have a nice day')
                    return
            else:
                print_pause('Fine be that way, have a nice day')
                return
        else:
            print_pause('Fine be that way, have a nice day')
            return
    else:
        print_pause('Fine be that way, have a nice day')

intro()
First_choice()