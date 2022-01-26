# Absolute File Path:

file_path = 'C:/Users/felip/python_work/notebooks/bk_Python_crash_course/10_files_and_exceptions/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents.rstrip())
