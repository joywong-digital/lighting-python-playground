""" 
Joy's first python program
"""

colour_temp=input("What colour temperature do you want to set? ")
print("You are using " + colour_temp + "K as your colour temperature in the room.")

# Practicing format strings

ceiling_height=input("What is the ceiling height of the room? ")
print(f"The ceiling height of the room is {ceiling_height} meters.")

# Practicing string functions

space_name=input("What's the space name? ").strip().title()
print(f"The space you are designing for is {space_name}.")

# Practicing string functions

lobby_type=input("What type of lobby is it? ").strip().lower()
first, last=lobby_type.split(" ")
print(f"You are designing a {first} lobby now")

# Practicing addition and conversion from str to int

Ambient_light=input("What is the ambient light level in lux? ")
Accent_light=input("What is the accent light level in lux from spotlight only?")
Total_light=int(Ambient_light)+int(Accent_light)
print (f"The lux level on art work is {Total_light} lux")

# Practicing nesting of function calls

print("(Below is the same as above but with nesting of function calls)")
Ambient_light=int(input("What is the ambient light level in lux? "))
Accent_light=int(input("What is the accent light level in lux from spotlight only?"))
Total_light=Ambient_light+Accent_light
print (f"The lux level on art work is {Total_light} lux")

# Practicing float (with decimal places) instead of int

false_ceiling_height=float(input("What is the false ceiling height of the room? "))
ceiling_void=float(input("What is the ceiling void height of the room? "))
total_ceiling_height=false_ceiling_height+ceiling_void
print (f"The clear ceiling height is {total_ceiling_height} meters.")

# Practicing round up and simplier code with fewer variables

print("(Below is the same as above but round up decimal places)")
false_ceiling_height=float(input("What is the false ceiling height of the room? "))
ceiling_void=float(input("What is the ceiling void height of the room? "))
total_ceiling_height=round(false_ceiling_height+ceiling_void)

print (f"The clear ceiling height is {total_ceiling_height} meters.")

# Practicing formatting numbers with commas and decimal places

firstfloor_area=float(input("What is the first floor area? "))
secondfloor_area=float(input("What is the second floor area? "))

total_area=round(firstfloor_area+secondfloor_area)

print(f"{total_area:,.2f} square meters is the total area of the building.")

#Practicing division with rounding after decimal point

firstfloor_area=float(input("What is the first floor area? "))
firstfloor_nr_of_light=float(input("How many luminiare on first floor?"))

lightnr_firstfloor=round(firstfloor_area/firstfloor_nr_of_light)

print(f"There are {lightnr_firstfloor} luminiare per square meter.")

# Demonstrates defining a function without parameters
def lighting_term():
    print("is a lighting parameter that you need to know when you design a lighting scheme.")
    
word=input("Provide a lighting term: ")
print(word, end=" "), lighting_term()

# Demonstrates defining a function with parameters
def lighting_term(x):
    print(x, "is a lighting parameter that you need to know when you design a lighting scheme.")

y=input("Tell me a lighting term: ")
lighting_term(y)

# Demonstrates defining a function with a parameter with a default value
 
def office_lux(x="300"):
     print("The recommended lux level for an office is", x, "lux")

office_lux()
y=input("What is the lux level for the office you are designing?")
office_lux(y)

# Demonstrates defining a main function

def main():
    lux=input("Enter the lux level: ")
    write(lux)
    
def write(x="150"):
    print("The recommended lux level for corridor is", x, "lux")

main()

# Demonstrates defining a main function

def main():
    x=int(input("what's X?"))
    print("x squared is", square(x))
    
def square(n):
    return n * n

main()