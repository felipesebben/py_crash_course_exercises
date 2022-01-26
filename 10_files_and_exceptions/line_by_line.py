# Reading Line by Line
# You can use a for loop on the file object to examine each line from a file:

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

# Remove blank lines:

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
