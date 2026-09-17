"""
CS50P Week 4 - lighting playbook

Based on https://cdn.cs50.net/python/2022/x/lectures/4/src4.pdf

"""

# Demonstrates statistics - average.py

import random
import statistics

print("Measured lux average:", statistics.mean([100, 90]))

# Demonstrates import and random.choice - generate0.py

Colour_temp = random.choice(["Warm white", "cool white"])
print(Colour_temp)

# Demonstrates from - generate1.py

from random import choice

Ceiling_light_tech = choice(["Downlight", "Light cove", "Pendant", "Track light", "Chandelier"])
print(Ceiling_light_tech)

# Demonstrates randint - generate2.py

Warm_white_range = random.randint(2700, 3000)
print(Warm_white_range)

# Demonstrates shuffle - generate3.py

colour_temp = ["Warm White", "Cool White", "Neutral White"]
random.shuffle(colour_temp)
for colour in colour_temp:
    print(colour)
    
# Demonstrates pip-installed package - say0.py

import cowsay  # type: ignore
import sys

cowsay.cow("I love Lighting!")

# Demonstrates a t-rex - say1.py

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex(sys.argv[1] + ", I need good lighting too!")