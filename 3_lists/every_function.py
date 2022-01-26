list = ['excel','word','python','SQL','tableau']
print(list)


# - What is a list?
#1) accessing elements in a list:

print(list[1])

#formatting:
print(list[1].title())

print(list[-1].title())

#2) using individual values from a list:

message = f"The first Data Analysis program that I learned was {list[0].title()}."
print(message)

# - Changing, adding and removing elements.

#1) Modifying elements in a list:
print(list)
list[0] = 'power point'
print(list)

#2) Adding elements to a list

	#2.a) appending elements to a list:

print(list)
list.append('r')
list.append('excel')
list.append('java')
print(list)

	#2.b) inserting elements into a list:

list.insert(1, 'css')
print(list)

#3) Removing elements from a list:

	#3.a) Removing an item using the del statement:

print(list)
del list[0]
print(list)

	#3.b) Removing an intem using the pop() method:

print(list)
popped_list = list.pop()
print(popped_list)

print(list)
last_program = list.pop()
print(f"\nThe last program I've studied is {last_program.title()}.")

	#3.c) Popping Items from any Position in a List

print(list)

first_program = list.pop(0)
print(f"\nThe first program that I've studied is {first_program.upper()}.")

print(list)
list.remove('word')
print(list)

too_difficult = 'r'
list.remove(too_difficult)
print(list)
print(f"\nLearning {too_difficult.upper()} is way too hard right now.")


#4) Organizing a List:

	#4.a) Sorting a List Permanently with the sort() Method:

list = ['excel','word','python','SQL','tableau']
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

	#4.b) Sorting a List Temporarily with the sorted() Function:

list = ['excel','word','python','SQL','tableau']
print("\nHere is the original list:")
print(list)

print("\nHere is the sorted list:")
print(sorted(list))

print("\nHere is the original list again:")
print(list)

#5) Printing a List in Reverse Order:

print(list)
list.reverse()
print(list)

#6) Finding the Length of a List:

print(len(list))