#Replace Element: Given a list, replace the first occurrence of a specified element with another element. 
numbers = [1, 2, 3, 4, 5, 3]  # Example list
old_element = 3  # Element to replace
new_element = 99  # New element to insert

# Check if the element exists in the list
if old_element in numbers:
    index=numbers.index(old_element)
    numbers[index]=new_element
    print("Updated list: ", numbers)
else:
    print(f"{old_element} has not been found")    