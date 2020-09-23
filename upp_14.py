FRUITS = ['banana', 'apple', 'orange']
CARS = ['volvo', 'ford', 'tesla']
STUFF = ['Wallet', 'footrest', 'sofa']

def run():
    basket = [
        'volvo', 'is', 'an', 'orange', 'sofa', 'apple', 'footrest'
    ]
    cars = []
    fruits = []
    stuff = []
    rest = []
    for item in basket:
        if item in CARS:
            cars.append(item)
        elif item in FRUITS:
            fruits.append(item)
        elif item in STUFF:
            stuff.append(item)
        else:
            rest.append(item)
    write_things(cars, 'Cars')
    write_things(fruits, 'Fruits')
    write_things(rest, 'Misc')
    write_things(stuff, 'Stuff')


def write_things(items, kind):
    print(f"{kind.upper()} {len(items)}")
    for item in items:
        print(f" {item}")


if __name__ == '__main__':
    run()
