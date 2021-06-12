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
    
menu_control = 1

while menu_control > 0:
    print('\nWhat concept do you need to solve?')
    choice = int(input('\nEnter \n(1) for Equations of Motion \n(2) to Quit\n'))
    if choice == 2:
        menu_control = -1
        break
    elif choice == 1:
        print('\nWhat quantity do you need to find?')
        quantity_choice = int(input('\nEnter \n(1) to find final velocity \n(2) to find inital velocity \n(3) to find displacement \n(4) to find acceleration \n(5) to find time taken for motion \n(6) to quit\n'))
        if quantity_choice == 6:
            menu_control = -1
            break
        elif quantity_choice == 1:
            find_final_velocity()
            continue
        elif quantity_choice == 2:
            find_inital_velocity()
            continue
        elif quantity_choice == 3:
            
            continue
        elif quantity_choice == 4:
            
            continue
        elif quantity_choice == 5:
            
            continue

