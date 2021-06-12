from calc import find_inital_velocity, find_final_velocity, find_acc, find_displacement

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
            find_displacement()
            continue
        elif quantity_choice == 4:
            find_acc()
            continue
        elif quantity_choice == 5:
            
            continue

