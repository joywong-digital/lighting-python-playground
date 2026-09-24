"""
CS50P Week 5 - Lighting Playbook

Inspired by CS50P Lecture 5: Unit Tests https://cdn.cs50.net/python/2022/x/lectures/5/src5.pdf

Example: Classify colour temperature (CCT)
commonly used in lighting design.

"""

def cct_type(kelvin):
    """Return lighting description based on colour temperature."""

    if kelvin <= 3000:
        return "Warm White"
    elif kelvin <= 4000:
        return "Neutral White"
    else:
        return "Cool White"


def main():
    kelvin = int(input("Enter colour temperature (K): "))
    print(f"Classification: {cct_type(kelvin)}")


if __name__ == "__main__":
    main()
    

""" Test file """

from CS50P_Week5_lighting import cct_type

def test_warm_white():
    assert cct_type(2700) == "Warm White"


def test_neutral_white():
    assert cct_type(3500) == "Neutral White"


def test_cool_white():
    assert cct_type(5000) == "Cool White"