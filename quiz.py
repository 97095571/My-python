import random
randomGetal = random.randint(1,100)
getal = 0
aantalBeurten = 0 
print (randomGetal)

while getal != randomGetal:
    getal = int(input("Raad het getal: "))
    aantalBeurten += 1


print(f"gefeliciteerd je hebt getal geraden in {aantalBeurten} beurten")