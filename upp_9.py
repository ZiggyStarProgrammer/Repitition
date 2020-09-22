import random


def game():
    ranger = input("Hur många uppgifter vill du lösa?")
    rango = int(ranger)
    correct_answers = 0
    q_b = input("Största tal? ")
    biggest = int(q_b)
    for i in range(rango):
        a = random.randint(1, biggest)
        b = random.randint(1, biggest)
        answer = input(str(a) + "+" + str(b) + "=")
        number = int(answer)
        if number == a + b:
            print("Rätt!")
            correct_answers += 1
        else:
            print(f"Fel... Det blir {a+b}")
            print("---")

    print(f"Du fick {str(correct_answers)} av {ranger} rätt.")


if __name__ == '__main__':
    game()
