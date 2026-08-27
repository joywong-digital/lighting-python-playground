"""
CS50P Week 1 - lighting playbook

Based on https://cdn.cs50.net/python/2022/x/lectures/1/src1.pdf

"""
#1 Demonstrates conditionals

x = int(input("What's the height of the entrance lobby? "))
y = int(input("What's the height of the lift lobby? "))

if x > y:
    print("The entrance lobby is taller than the lift lobby.")
if x < y:
    print("The entrance lobby is lower than the lift lobby")
if x == y:
    print("The entrance lobby and lift lobby are the same height")


#2 Demonstrates mutually exclusive conditions

x = int(input("What is the size of the room (part of the escape route)?"))

if x > 6:
    print("The room requires 2 emergency lighting based on IS3217 system integrity.")
elif x < 6:
    print("The room may use an internally illuminated exit sign to fulfill IS3217 system integrity.")
elif x == 6:
    print("The room requires 2 emergency lighting based on IS3217 system integrity.")
    
#3 Demonstrates fewer conditions

x = int(input("What is the size of the room (part of the escape route)?"))

if x > 6:
    print("The room requires 2 emergency lighting based on IS3217 system integrity.")
elif x < 6:
    print("The room may use an internally illuminated exit sign to fulfill IS3217 system integrity.")
else:
    print("The room requires 2 emergency lighting based on IS3217 system integrity.")
    
#4 Demonstrates inequalities and logical operator
#5 Demonstrates equality
#6 Demonstrates equality

x = int(input("What's the size of the room (part of the escape route)?"))

if x >6 or x == 6:
     print("The room requires 2 emergency lighting based on IS3217 system integrity.")
else:
     print("The room may use an internally illuminated exit sign to fulfill IS3217 system integrity.")

# 7 Demonstrates inequalities and logical operators
# 8 Demonstrates inequalities and logical operators

kelvin = int(input("Colour Temperature(K):"))

if kelvin >= 2700 and kelvin <= 3000:
     print("The colour temperature is warm white.")
elif kelvin > 3000 and kelvin <= 4000:
     print("The colour temperature is neutral white.")
else:
     print("The colour temperature is cool white.")
     
# 9 Demonstrates chained comparisons

kelvin = int(input("Colour Temperature(K):"))

if 2700 <= kelvin <= 3000:
     print("The colour temperature is warm white.")
elif 3000 < kelvin <= 4000:
     print("The colour temperature is neutral white.")
else:
     print("The colour temperature is cool white.")

# 10 Demonstrates fewer comparisons

kelvin = int(input("Colour Temperature(K):"))

if kelvin >= 2700:
     print("The colour temperature is warm white.")
elif kelvin >= 4000:
     print("The colour temperature is neutral white.")
else:
     print("The colour temperature is cool white.")
     
# 11 Compares strings

answer = input("Do you agree to use warm white lighting? ")
if answer == "yes":
    print("Use warm white lighting.")
else:
    print("Use neutral or cool white lighting.")
    
# 12 Strips string before comparing
"""
strip() method removes any leading and trailing whitespace from the user's input
"""

answer = input("Do you agree to use warm white lighting? ").strip()
if answer == "yes":
    print("Use warm white lighting.")
else:
    print("Use neutral or cool white lighting.")
    
# 13 Lowercases string before comparing

"""
.strip() removes extra spaces.
.lower() converts the input to lowercase.
"""

answer = input("Do you agree to use warm white lighting? ").strip().lower()
if answer == "yes":
    print("Use warm white lighting.")
else:
    print("Use neutral or cool white lighting.")
    
# 14 Compares multiple strings

answer = input("Do you agree to use warm white lighting? ").strip().lower()
if answer == "yes" or answer == "y":
    print("Use warm white lighting.")
else:
    print("Use neutral or cool white lighting.")
    
# 15 Compares multiple strings

answer = input("Do you agree to use warm white lighting? ").strip().lower()
if answer.startswith("y"):
    print("Use warm white lighting.")
else:
    print("Use neutral or cool white lighting.")
    
# 16 emonstrates modulo operator

x = input("What's traffic light signal now? (Green/ Red)").strip()

if x == "green":
    print("go")
else:
    print("stop")

# 17 Demonstrates a function that returns a bool

def main():
    x = int(input("Is 3000K a warm white colour temperature? (Enter 1 for Yes, 0 for No): "))
    if colour(x):
        print("Yes, 3000K is a warm white colour temperature.")
    else:
        print("You are not correct. 3000K is a warm white colour temperature.")


def colour(n):
    if n == 1:
        return True
    else:
        return False

main()

# 18 Demonstrates conditional expressions (ternary operators)

def main():
    x = int(input("Is 5000K a cool white colour temperature? (Enter 1 for Yes, 0 for No): "))
    if colour(x):
        print("Yes, 5000K is a cool white colour temperature.")
    else:
        print("Wrong! 5000K is a cool white colour temperature.")


def colour(n):
    return True if n == 1 else False

main()

# 19 Demonstrates returning the value of a Boolean expression

def main():
    x = int(input("What is the size of the room?"))
    if room_size(x):
        print("The room requires 2 emergency lighting based on IS3217 system integrity.")
    else:
        print("The room may use an internally illuminated exit sign to fulfill IS3217 system integrity.")


def room_size(n):
    return n >= 6


main()

# 20 Compares multiple strings with if/elif/else

colour = input("What's the colour temperature in K? ").strip().lower()

if colour == "2700":
    print("warm white")
elif colour == "3000":
    print("warm white")
elif colour == "4000":
    print("neutral white")
else:
    print("cool white")
    
# 21 Uses or

colour = input("What's the colour temperature in K? ").strip().lower()

if colour == "2700" or colour == "3000":
    print("warm white")
elif colour == "4000":
    print("neutral white")
else:
    print("cool white")

# 22 Uses match with case
# 23 Uses |

name = input("What's the colour temperature in K? ").strip().lower()

match name:
    case "2700" | "3000":
        print("warm white")
    case "4000":
        print("neutral white")
    case _:
        print("cool white")

