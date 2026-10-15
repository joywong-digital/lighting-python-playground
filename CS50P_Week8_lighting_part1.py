"""

Week 8_part 1:

Object-Oriented Programming

Tuple <> List <> Dictionary <> Class

https://cs50.harvard.edu/python/weeks/8/

"""
class Luminaire:
    def __init__(self, name, cct, cri):
        if not name:
            raise ValueError("Missing name")
        if not 1800 <= cct <= 6500:
            raise ValueError("CCT out of range")
        if not 0 <= cri <= 100:
            raise ValueError("Invalid CRI")
        self.name = name
        self.cct = cct
        self.cri = cri


def main():
    luminaire = get_luminaire()
    print(f"{luminaire.name}: {luminaire.cct}K, CRI {luminaire.cri}")


def get_luminaire():
    name = input("Name: ")
    cct = int(input("CCT (K): "))
    cri = int(input("CRI: "))
    return Luminaire(name, cct, cri)


if __name__ == "__main__":
    main()