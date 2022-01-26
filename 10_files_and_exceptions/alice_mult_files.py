def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filename = 'alice.txt'
count_words(filename)

filenames = [
             'alice.txt', '1984.txt', 'pride_prejudice.txt',
             'frankenstein.txt'
             ]

for filename in filenames:
    count_words(filename)
