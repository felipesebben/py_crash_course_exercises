favorite_numbers = {
    'amelia': [39, 47, 90, 30],
    'julio': [9, 11, 33, 20, 29],
    'rosangela': [7, 2, 3, 55],
    'mariana': [54, 17, 7],
    'vitor': [3, 5, 43],
}

for name, numbers in favorite_numbers.items():
    number = favorite_numbers.values()
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print(" " + str(number))
    

    