# Python Task 2 from Trello

## Task 
Program calculate year of birth!
Timings
30-60 Minutes

Summary
Cool, we've used strings to make a program that made a welcome message. Now let's use some numerical types.

Create program that calculates the year of birth.

Tasks
define the variables age and name
make a calculation for the year in which the person was born
print out "OMG <person>, you are <age> years old so you were born in <year>" with the correct values
Second Part
prompt the user for input and re-assign the variable age and name
figure out a way to account for if the persons birthday has already happened this year or not
Extra
go look into the library time
print out the amount of hour this person has lived
Acceptance Criteria
program defines the variable age and name
program prints the string "OMG <person>, you are <age> years old so you were born in <year>"


#### Task 1
```python
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
        age_in_hours = (age * 365) * 24
        print("You have also lived for at least {} hours!".format(age_in_hours))
    else:
        active = False

print("I hope this was informative!")
```