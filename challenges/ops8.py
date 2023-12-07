# Define the list
phrase_list = ["Embrace", "cosmic", "burritos", "of", "existence;", "dance", "with", "starlight", "in", "taco", "shells"]

# Using append() to add an element at the end
phrase_list.append("universe")
print("After append:", phrase_list)

# Using clear() to remove all elements
phrase_list.clear()
print("After clear:", phrase_list)

# Re-create the list
phrase_list = ["Embrace", "cosmic", "burritos", "of", "existence;", "dance", "with", "starlight", "in", "taco", "shells"]

# Using copy() to create a new list with the same elements
copied_list = phrase_list.copy()
print("Copied list:", copied_list)

# Using count() to count the occurrences of an element
count_cosmic = phrase_list.count("cosmic")
print("Count of 'cosmic':", count_cosmic)

# Using extend() to add elements from another list
additional_elements = ["and", "galaxies"]
phrase_list.extend(additional_elements)
print("After extend:", phrase_list)

# Using index() to find the index of an element
index_dance = phrase_list.index("dance")
print("Index of 'dance':", index_dance)

# Using insert() to insert an element at a specific index
phrase_list.insert(5, "groove")
print("After insert:", phrase_list)

# Using pop() to remove and return an element by index
popped_element = phrase_list.pop(8)
print("Popped element:", popped_element)

# Using remove() to remove the first occurrence of an element
phrase_list.remove("cosmic")
print("After remove:", phrase_list)

# Using reverse() to reverse the order of elements
phrase_list.reverse()
print("After reverse:", phrase_list)

# Using sort() to sort the elements alphabetically
phrase_list.sort()
print("After sort:", phrase_list)
