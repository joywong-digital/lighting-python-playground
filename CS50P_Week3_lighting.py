"""
CS50P Week 3 - lighting playbook

Based on https://cdn.cs50.net/python/2022/x/lectures/3/src3.pdf

"""

# Gets a number from the user - number0.py

colour_temp = int(input("What is the Kelvin of warm white?"))
print(f"{colour_temp} K is a warm white colour temperature.")

# Catches a ValueError - number1,2.py

try:
    colour_temp = int(input("What is the Kelvin of warm white?"))
    print(f"{colour_temp} K is a warm white colour temperature.")
except ValueError:
    print("It is not an integer")

# Demonstrates else - number3.py

try:
    colour_temp = input("What's the Kelvin of warm white? ")
    colour_temp = int(colour_temp)
except ValueError:
    print(f"{colour_temp} is not an integer")
else:
    print(f"Warm white is {colour_temp}K")
    
# Adds a loop - number4.py

while True:
    try:
        colour_temp = int(input("What's the Kelvin of warm white? "))
    except ValueError:
        print("That is not an integer")
    else:
        break

print(f"Warm white is {colour_temp}K")

# Adds functions, uses break and return - number5.py


def main():
    column_height = get_int()
    print(f"Column height is {column_height}m")


def get_int():
    while True:
        try:
            x = int(input("What's the column height? "))
        except ValueError:
            print("That is not an integer")
        else:
            break
    return x

main()

# Removes break - number6.py

def main():
    column_height = get_int()
    print(f"Column height is {column_height}m")


def get_int():
    while True:
        try:
            x = int(input("What's the column height? "))
        except ValueError:
            print("That is not an integer")
        else:
            return x

main()

# Removes else - number7.py

def main():
    column_height = get_int()
    print(f"Column height is {column_height}m")

def get_int():
    while True:
        try:
            return int(input("What's the column height? "))
        except ValueError:
            print("That is not an integer")

main()

# Adds pass - number8.py

def main():
    column_height = get_int()
    print(f"Column height is {column_height}m")


def get_int():
    while True:
        try:
            return int(input("What's the column height? "))
        except ValueError:
            pass

main()

# Adds prompt - number9.py


def main():
    column_height = get_int("What's the column height? ")
    print(f"Column height is {column_height}m")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()