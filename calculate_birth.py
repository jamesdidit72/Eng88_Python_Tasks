active = True
while active:
    continue_ = input("Do you wish to continue? Y/N ")
    name = input("What is your name?  ")  # asks the use what their name is
    age = int(input("How old are you?  "))  # asks the user how old they are
    if continue_.upper() == "Y":
        birthday_passed = input("has your birthday already passed? Y/N ")
        if birthday_passed.upper() == "Y":
            current_year = 2022
        else:
            current_year = 2021
        years = current_year - age  # calculates the age
        print("OMG {}, you are {} years old so you were born in {}".format(name, age, years))  # prints out a statement containing the variables
    else:
        active = False

print("I hope this was informative!")
