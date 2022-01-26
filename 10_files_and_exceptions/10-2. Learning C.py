# Read in each line from the file learning_python and replace the word Python
# with the name of another language. Print each modified line to the screen.

filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    # Remove newline, then replace Python with C.
    line = line.rstrip()
    print(line.replace('Python', 'C'))
