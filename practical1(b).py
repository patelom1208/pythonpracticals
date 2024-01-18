# Given list
List1 = [1, 2, 3, 4, ["python", "java", "c++", [10, 20, 30]], 5, 6, 7, ["apple", "banana", "orange"]]

# Get the word "orange" and "Python"
word_orange = List1[-1][-1]
word_python = List1[4][0].capitalize()  # Capitalize the first letter

# Print the words
print("Word 'orange':", word_orange)
print("Word 'Python':", word_python)

# Repeat the list five times without using loops
RepeatedList = [List1] * 5

# Print the repeated list
print("Repeated List five times:")
print(RepeatedList)


original_list = [1,2,3,4,5,6]
copied_list = original_list[:]

original_list [0] = 99
print ("Original list",original_list)
print ("Copied List",copied_list)