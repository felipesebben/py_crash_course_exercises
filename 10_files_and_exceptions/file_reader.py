# Reading an Entire File:

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

# File Paths:
with open(
    'Python_crash_course/10_files_and_exceptions/pi_digits.txt'
         ) as file_object:
    contents = file_object.read()
print(contents.rstrip())

