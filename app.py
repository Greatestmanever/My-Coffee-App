import database

# Define a new prompt for the users
MENU_PROMPT = """ -- Coffee Bean App --

Please choose one of these options:

1) Add a new bean.
2) See all beaans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Exit.

Your Selection:"""

# Users  interaction menu
def menu():
    connection = database.connect()
    database.create_tables(connection)

    #Using while loop
    while (user_input := input(MENU_PROMPT)) != "5":
        # Using if, elif, else statement
        if user_input == "1":
           prompt_add_new_bean(connection)

        elif user_input == "2":
            prompt_see_all_beans(connection)

        elif user_input == "3":
            prompt_find_bean(connection)

        elif user_input == "4":
            prompt_find_best_method(connection)
        else:
            print("Invalid input, please try again!")

#Users menu functions
def prompt_add_new_bean(connection):
    name = input("Enter bean name: ")
    method = input("Enter how you've prepared it: ")
    rating = int(input("Enter your rating between rating score (0-100): "))

    database.add_bean(connection, name, method, rating)


def prompt_see_all_beans(connection):
    beans = database.get_all_beans(connection)

    for bean in beans:
        print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")


def prompt_find_bean(connection):
    name = input("Enter bean name to find: ")
    beans = database.get_beans_by_name(connection, name)
        
    for bean in beans:
        print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")


def prompt_find_best_method(connection):
    name = input("Enter bean name to find: ")
    best_method = database.get_best_preparation_for_bean(connection, name)

    print(f" The preparation method for {name} is: {best_method[2]}.")


#menu function to verify the code works
menu()