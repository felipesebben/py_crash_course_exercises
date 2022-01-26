# Modify your block in Exercise 10-8 to fail silently if any file is missing.


filenames = ['cats.txt', 'dogs.txt', 'birds.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()

    except FileNotFoundError:
        pass
    else:
        print(f"\nPrinting file: {filename}.")
        print(contents)
