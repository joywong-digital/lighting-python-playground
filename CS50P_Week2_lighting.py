"""
CS50P Week 2 - lighting playbook

Based on https://cdn.cs50.net/python/2022/x/lectures/2/src2.pdf

"""

# Demonstrates indexing into a list (src2.pdf - p.13)

Lightingtypes = ["Downlight", "Floor Lamp", "Track Light"]

print(Lightingtypes[0])
print(Lightingtypes[1])
print(Lightingtypes[2])

# Demonstrates iterating over a list (src2.pdf - p.14)

Lightingtypes = ["Downlight", "Floor Lamp", "Track Light"]

for lightingtype in Lightingtypes:
    print(lightingtype)
    
# Demonstrates iterating over and indexing into a list (src2.pdf - p.15)

Lightingtypes = ["Downlight", "Floor Lamp", "Track Light"]

for i in range(len(Lightingtypes)):
    print(i + 1, Lightingtypes[i])
    
    
# Demonstrates indexing into a dict (src2.pdf - p.16)

lightsource = {
    "Metal halide": "Discharge lamp",
    "High pressure sodium": "Discharge lamp",
    "LED": "Solid state lighting",
}

print(lightsource["Metal halide"])
print(lightsource["High pressure sodium"])
print(lightsource["LED"])

# Demonstrates iterating over and index into a dict (src2.pdf - p.17)

lightsource = {
    "Metal halide": "Discharge lamp",
    "High pressure sodium": "Discharge lamp",
    "LED": "Solid state lighting",
}

for source in lightsource:
    print(source, lightsource[source], sep=", ")

# Demonstrates iterating over a list of dict objects (src2.pdf - p.18)

lightsource = [
    {"name": "Metal halide", "type": "Discharge lamp", "Efficiency": "Medium"},
    {"name": "High pressure sodium", "type": "Discharge lamp", "Efficiency": "High"},
    {"name": "LED", "type": "Solid state lighting", "Efficiency": "Very High"},
]

for source in lightsource:
    print(source["name"], source["type"], source["Efficiency"], sep=", ")

# Prints a lighting column (src2.pdf - p.19)

print("💡")
print("💡")
print("💡")

# Prints column of lights using a loop (src2.pdf - p.20)

for _ in range(3):
    print("💡")
    
# Prints column of lights using a function with a loop (src2.pdf - p.21)

def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("💡")

main()

# Prints column of lights using a function with str multiplication (src2.pdf - p.22)

def main():
    print_column(3)

def print_column(height):
    print("💡\n" * height, end="")

main()

# Prints row of lights using a function with str multiplication (src2.pdf - p.23)

def main():
    print_row(4)

def print_row(width):
    print("💡" * width)

main()

# Prints light box using a function with nested loops (src2.pdf - p.24)

def main():
    print_light_box(3)

def print_light_box(size):
    for i in range(size):
#can use _ instead of i if you don't need to use the variable
        for j in range(size):
#can use _ instead of j if you don't need to use the variable
            print("💡", end="")
        print()

main()

# Prints light box using a function with a loop and str multiplication (src2.pdf - p.25)

def main():
    print_light_box(3)


def print_light_box(size):
    for _ in range(size):
        print("💡" * size)

main()

# Prints square of bricks using a function with a loop and str multiplication (src2.pdf - p.26)

def main():
    print_lightbox(3)

def print_lightbox(size):
    for _ in range(size):
        print_row(size)

def print_row(width):
    print("💡" * width)

main()