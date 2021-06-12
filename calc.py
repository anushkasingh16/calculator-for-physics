import math
import os

clear = lambda: os.system('clear') #system call to clear the screen 

def find_final_velocity():
    inital_velocity = int(input('\nEnter inital velocity: '))
    acceleration = int(input('\nEnter acceleration: '))
    third_var_choice = input('\nEnter D if you have displacement or T if you have time taken given to you: ')
    if third_var_choice == 'D':
        displacement = int(input('\nEnter displacement: '))
        result = math.pow((2*acceleration*displacement+math.pow(inital_velocity,2)),0.5)  
    elif third_var_choice == 'T':
        time_taken = int(input('\nEnter time taken: '))
        result = inital_velocity + acceleration*time_taken;
    else:
        print('\nIncorrect choice selected.')
    clear()
    print('\nThe FINAL VELOCITY is : ',result)

def find_inital_velocity():
    acceleration = int(input('\nEnter acceleration: '))
    first_var_choice = input('\nEnter Y if you are given final velocity or N if not: ')
    if first_var_choice == 'Y':
        final_velocity = int(input('\nEnter final velocity: '))
        second_var_choice = input('\nEnter D if you have displacement or T if you have time taken given to you: ')
        if second_var_choice == 'D':
             displacement = int(input('\nEnter displacement: '))
             result = math.pow(final_velocity,2)-2*acceleration*displacement
             if result < 0:
                 result = 'ERROR'
             else:
                result = math.pow(math.pow(final_velocity,2)-2*acceleration*displacement,0.5)
        elif second_var_choice == 'T':
            time_taken = int(input('\nEnter time taken: '))
            result = final_velocity - acceleration*time_taken
        else:
            print('\nIncorrect choice selected.')
    elif first_var_choice == 'N':
        time_taken = int(input('\nEnter time taken: '))
        displacement = int(input('\nEnter displacement: '))
        result = (displacement-0.5*acceleration*math.pow(time_taken,2))/time_taken
    else:
        print('\nIncorrect choice selected.')
    clear()
    if result != 'ERROR':
        print('\nThe INITAL VELOCITY is : ',result)
    else:
         print('\nThe result is the root of a negative number, and thus cannot be calcualted.')
    
def find_acc():
    inital_velocity = int(input('\nEnter inital velocity: '))
    first_var_choice = input('\nEnter Y if you are given final velocity or N if not: ')
    if first_var_choice == 'Y':
        final_velocity = int(input('\nEnter final velocity: '))
        second_var_choice = input('\nEnter D if you have displacement or T if you have time taken given to you: ')
        if second_var_choice == 'D':
             displacement = int(input('\nEnter displacement: '))
             result = (math.pow(final_velocity,2)-math.pow(inital_velocity,2))/(2*displacement)
        elif second_var_choice == 'T':
            time_taken = int(input('\nEnter time taken: '))
            result = (final_velocity - inital_velocity)/time_taken
        else:
            print('\nIncorrect choice selected.')
    elif first_var_choice == 'N':
        displacement = int(input('\nEnter displacement: '))
        time_taken = int(input('\nEnter time taken: '))
        result = (2*(displacement - inital_velocity*time_taken))/(math.pow(time_taken,2))
    else:
        print('\nIncorrect choice selected.')
    clear()
    print('\nThe ACCELERATION is : ',result)

def find_displacement():