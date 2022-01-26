multiples_of_ten = input("Please provide a number: ")
multiples_of_ten = int(multiples_of_ten)

if multiples_of_ten % 10 == 0:
    print(f"\nThis number is a multiple of 10!")
else:
    print(f"\nThis number is not a multiple of 10.")