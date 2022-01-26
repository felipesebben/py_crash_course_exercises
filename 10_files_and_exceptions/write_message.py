filename = 'programming.txt'

with open(filename, 'w') as file_object:  # 'w' -> open the file in write mode
    file_object.write("I love programming.")

# Writing Multiple Lines:

with open(filename, 'w') as file_object:  # 'w' -> open the file in write mode
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# Appending to a File:

with open(filename, 'a') as file_object:  # 'a' -> opeh the file in append mode
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I also love creating apps that can run in a browser.\n")
