#creates an empty list
list1 = []
list2= ['om','daddy','jarvis','ironman','universal']
#print the above list
print (list2)

#prints the length of the list
print (len(list2))

# Example list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get the first item
first_item = my_list[0]

# Get the middle item (assuming the list has an odd length)
middle_item = my_list[len(my_list) // 2]

# Get the last item
last_item = my_list[-1]

# Print the results
print("First item:", first_item)
print("Middle item:", middle_item)
print("Last item:", last_item)
#prints the list
mixed_datatype=['OM','21','5.8','ITS COMPLICATED','GODHRA']
print(mixed_datatype)
#printa the list
IT_COMPANIES=['Facebook','Google','Microsoft','Apple','IBM','ORACLE','AMAZON']
print(IT_COMPANIES)
#print the length 
print(len(IT_COMPANIES))

# Get the first item
first_item = IT_COMPANIES[0]

# Get the middle item (assuming the list has an odd length)
middle_item = IT_COMPANIES[len(my_list) // 2]

# Get the last item
last_item = IT_COMPANIES[-1]

# Print the results
print("First item:", first_item)
print("Middle item:", middle_item)
print("Last item:", last_item)

IT_COMPANIES [0]= 'Universal'
print (IT_COMPANIES)

# 11 add IT Companies to the itcompanies 
IT_COMPANIES.append('Webosphere')
print(IT_COMPANIES)

# 12 Insert an IT company in the middle of the companies list
IT_COMPANIES.insert(4,'INFINITE')

# 13 Change one of the it_companies names to uppercase (IBM excluded!)
IT_COMPANIES[IT_COMPANIES.index('Universal')] = IT_COMPANIES[IT_COMPANIES.index('Universal')].upper()
print(IT_COMPANIES)

#14 To join the elements of the list it_companies with a string '#; ', you can use the join() method. Here is an example:
companies_str = '#; '.join(IT_COMPANIES)
print(companies_str)

#15 Check if a certain company exists in the it_companies list.
company_to_check = "Microsoft"

if company_to_check in IT_COMPANIES:

    company_to_check = "Microsoft"
    print(f"{company_to_check} exists in the list of IT companies.")
else:
    print(f"{company_to_check} does not exist in the list of IT companies.")
#16 Sort the list using sort() method
    # Sample list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Sorting the list in-place using sort()
my_list.sort()

# Displaying the sorted list
print("Sorted List:", my_list)

#17 Reverse the list in descending order using reverse() method
# Sample list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Sorting the list in descending order in-place using sort()
my_list.sort(reverse=True)

# Displaying the sorted list
print("Sorted List (Descending):", my_list)

#18 Slice out the first 3 companies from the list
first_three_companies = IT_COMPANIES[:3]
print(first_three_companies)

#19 Slice out the last 3 companies from the list
last_three_companies = IT_COMPANIES[-3:]
print(last_three_companies)

# 20
middle_index = len(IT_COMPANIES) // 2

# Check if the length of the list is even or odd
if len(IT_COMPANIES) % 2 == 0:
    # If even, slice out the middle two companies
    middle_companies = IT_COMPANIES[middle_index - 1:middle_index + 1]
else:
    # If odd, slice out the middle company
    middle_companies = [IT_COMPANIES[middle_index]]

# Displaying the sliced list
print("Middle Company/Companies:", middle_companies)

# 21 Remove the first IT company from the list
removed_company = IT_COMPANIES.pop(0)
print(IT_COMPANIES)
#22 Remove the middle IT company or companies from the list
IT_COMPANIES.pop(middle_index)
print(IT_COMPANIES)

#23 Remove the last IT company from the list
removed_company = IT_COMPANIES.pop()
print("Removed Last Company:", removed_company)

#23 Remove all IT companies from the list
IT_COMPANIES.clear()
print(IT_COMPANIES)

#24 Destroy the IT companies list
del IT_COMPANIES

#25& 26 
# Given lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

# Joining the lists
joined_list = front_end + back_end

# Displaying the joined list
print("Joined List:", joined_list)

# Copying the joined list
full_stack = joined_list.copy()

# Inserting 'Python' and 'SQL' after 'Redux'
index_of_redux = full_stack.index('Redux')
full_stack[index_of_redux + 1:index_of_redux + 1] = ['Python', 'SQL']

# Displaying the updated full_stack list
print("Updated full_stack List:", full_stack)

# LEVEL 2 
# List of 10 students ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
min_age = min(ages)
max_age = max(ages)

# Add the min age and the max age again to the list
ages.extend([min_age, max_age])

# Find the median age
middle_index = len(ages) // 2
median_age = (ages[middle_index - 1] + ages[middle_index]) / 2 if len(ages) % 2 == 0 else ages[middle_index]

# Find the average age
average_age = sum(ages) / len(ages)

# Find the range of the ages
age_range = max_age - min_age

# Compare the value of (min - average) and (max - average), use abs() method
min_difference = abs(min_age - average_age)
max_difference = abs(max_age - average_age)

# List of countries
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# Find the middle country(ies) in the countries list
middle_index = len(countries) // 2
middle_countries = [countries[middle_index]] if len(countries) % 2 != 0 else [countries[middle_index - 1], countries[middle_index]]

# Divide the countries list into two equal lists if it is even, if not, one more country for the first half
first_half, second_half = countries[:middle_index], countries[middle_index:]

# Displaying the results
print("Sorted Ages:", ages)
print("Min Age:", min_age)
print("Max Age:", max_age)
print("Median Age:", median_age)
print("Average Age:", average_age)
print("Age Range:", age_range)
print("Min Difference from Average:", min_difference)
print("Max Difference from Average:", max_difference)
print("Middle Country(ies):", middle_countries)
print("First Half of Countries:", first_half)
print("Second Half of Countries:", second_half)



