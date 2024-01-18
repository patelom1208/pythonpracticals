'''
# Create an initial list
my_list = [1, 3, 5, 7, 9]

# Append an element to the list
my_list.append(11)
print("After append:", my_list)

# Extend the list with another list
my_list.extend([13, 15, 17])
print("After extend:", my_list)

# Remove an element from the list
my_list.remove(5)
print("After remove:", my_list)

# Reverse the order of elements in the list
my_list.reverse()
print("After reverse:", my_list)

# Sort the list in ascending order
my_list.sort()
print("Ascending order:", my_list)

# Sort the list in descending order
my_list.sort(reverse=True)
print("Descending order:", my_list)
'''
carslist = ["Audi", "BMW", "MERCEDES", "VOLVO"]
print(carslist[-3:])