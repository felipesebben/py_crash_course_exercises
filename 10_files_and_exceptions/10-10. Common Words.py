# Visit Project Gutenberg and find a few texts you’d like to analyze.
# Download the text files for these works, or copy the raw text from your
# browser into a text file on your computer.
# You can use the count() method to find out how many times a word or phrase
# appears in a string.

def count_common_words(filename, word):
    """Count how many times word appears in the text."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, I cannot find the file {filename}.")
    else:
        # Count how many times a word or phrase appears in a string:
        word_count = contents.lower().count(word)

        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)


filename = 'ulisses.txt'
count_common_words(filename, 'the')
