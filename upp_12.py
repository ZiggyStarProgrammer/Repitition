def is_it_too_long(name, maxl):
    return len(name) > maxl


def main():
    try:
        maxl = int(input("Ange namnets maxlängd: "))
    except ValueError:
        maxl = 5

    students = input("Skriv ett namn: ").split(",")
    for name in students:
        if is_it_too_long(name, maxl):
            print(f"{name.title()} är för långt!")


if __name__ == '__main__':
    main()