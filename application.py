"""This is the factorial application"""
import os
import sys

def clean():
    """This function cleas the screen"""
    os.system("clear")
def out():
    """This function exit the program"""
    print "See you later"
    sys.exit()
clean()
print "Welcome to the application of factorial\n"
def question():
    """This function quest to the user if he want to insert another number"""
    clean()
    ques = True
    while ques == True:
        ans = raw_input("Do you want to see the factorial of another number? y/n\n")
        ans = ans.lower()
        if ans == "y" or ans == "yes":
            ques = False
            calculate()
        elif ans == "n" or ans == "no":
            ques = False
            out()
        else:
            raw_input("Choose a correct answer")
            clean()
            ques = True

def factorial(one, number):
    """This function makes the multiply for the factorial"""
    if number > 0 and number <= 995:
        one = factorial(one, number-1)
        one = one * number
    else:
        one = 1
    if number > 995:
        raw_input("This range is so high please  try again ")
        clean()
        calculate()
    return one
def calculate():
    """This function calculate the factorial and shows to the user"""
    fact = True
    while fact == True:
        try:
            num = int(raw_input("Insert a number in range of 1 to 995:\n"))
            result = factorial(1, num)
            print "The factorial of %s is: %s" %(num, result) + "\n"
            fact = False
            raw_input("Press enter")
            question()
        except ValueError:
            raw_input("Insert only integer numbers please")
            fact = True
            clean()
calculate()
