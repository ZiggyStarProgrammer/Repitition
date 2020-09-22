import random

antal_gissningar = 0
n = random.randint(1, 20)

while True:
    text = input("Gissning: ")
    as_number = int(text)
    if as_number == n:
        print(f"Korrekt! \n"
              f"Antal gissningar: {antal_gissningar}")
        break

    if as_number < n:
        print("Fel, högre!")
        antal_gissningar += 1

    if as_number > n:
        print("Fel, lägre!")
        antal_gissningar += 1
