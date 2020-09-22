import random

n = random.randint(1, 20)

while True:
    text = input("Your guess: ")
    as_number = int(text)
    if as_number == n:
        print("Correct!")
        break

    if as_number < n:
        print("Wrong number, go higher!")

    if as_number > n:
        print("Wrong number, go lower!")
