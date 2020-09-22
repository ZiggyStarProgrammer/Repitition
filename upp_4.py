import random

antal_gissningar = 0
n = random.randint(1, 20)

while True:
    text = input("Gissning: ")
    as_number = int(text)
    if as_number == n:
        print("Korrekt", antal_gissningar)
        break

    if as_number < n:
        print("Fel, nummret är lägre!")
        antal_gissningar = antal_gissningar + 1

    if as_number > n:
        print("Fel, nummret är lägre")
        antal_gissningar = antal_gissningar + 1
