import random

n = random.randint(1, 3)
antal_gissningar = 0

def ask_number(antal_gissningar):
    antal_gissningar += 1
    text = input("Your guess: ")
    as_number = int(text)
    main(antal_gissningar, n, as_number)
    return as_number


def main(antal_gissningar, n, as_number):
    while True:
        if as_number == n:
            print("Correct!")
            print(antal_gissningar)
            break

        if as_number < n:
            print("Wrong number, go higher!")
            ask_number(antal_gissningar)

        if as_number > n:
            print("Wrong number, go lower!")
            ask_number(antal_gissningar)


ask_number(antal_gissningar)
