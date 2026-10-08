"""
CS50P Week 7 - Lighting Playbook

Inspired by CS50P Lecture 7 Regular expressions:  https://cdn.cs50.net/python/2022/x/lectures/7/src7.pdf

Example: Checking if a luminaire code/ tagging are correct

"""
import re

def main():
    code = input("Luminaire type: ").strip()
    if is_valid(code):
        print("Valid")
    else:
        print("Invalid")

def is_valid(code):
    # L or EX, then 2 digits, then an optional small letter
    # Valid: L01, L01a, EX01, EX01a
    # Invalid: L01A, L1, L01-, ex01
    return re.fullmatch(r"(L|EX)\d{2}[a-z]?", code) is not None

if __name__ == "__main__":
    main()