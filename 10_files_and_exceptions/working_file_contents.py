# Working with a File’s Contents
# Build a single string containing all the digits with no whitespace in it.

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

# Get rid of that by using strip() instead of rstrip():
pi_string2 = ''
for line in lines:
    pi_string2 += line.strip()

print(pi_string2)
print(len(pi_string2))
