#  Create fruits, vegetables, and animal products tuples join the three tuples and assign it to a variable called food_stuff_tp
fruits = ('Orange', 'Mango', 'Banana')
vegetables = ('LadiesFinger', 'tomoto', 'Potatoes')
animal_products = ('Meat', 'Chicken', 'Eggs')
food_stuff_tp = fruits + vegetables + animal_products









# Change the   food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

#  Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle_index = len(food_stuff_lt) // 2
middle_item_tp = food_stuff_tp[middle_index]
middle_items_lt = food_stuff_lt[middle_index-1:middle_index+2]
print("Middle Item Tuple: ", middle_item_tp)

# Slice out the first three items and the last three items from food_stuff_lt list
first_three_items_lt = food_stuff_lt[:3]
last_three_items_lt = food_stuff_lt[-3:]


# Display results after such operations
print("First Three Items from List:", first_three_items_lt)
print("Last Three Items from List:", last_three_items_lt)

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
if 'Estonia' in nordic_countries:
    print("Estonia is in the list of nordic country.")
else:
    print("Estonia is not in the list of nordic country.")

# Check if 'Iceland' is a nordic country
if 'Iceland' in nordic_countries:
    print("Iceland is in the list of nordic country.")
else:
    print("Iceland is not in the list of nordic country.")

