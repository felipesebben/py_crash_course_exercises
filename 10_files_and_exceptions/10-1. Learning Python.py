filename = 'learning_python.txt'

# Read Entire File:
print("- Reading in the entire file:")
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

# Loop through the entire object:
print("\n- Looping over the entire file:")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Store the lines in a list:
print("\n- Storing the lines in a list:")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
