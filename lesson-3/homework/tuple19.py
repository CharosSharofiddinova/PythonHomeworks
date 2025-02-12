#Remove Element by Value: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.
def remove_first_occurrence(tup, element):
    found = False
    new_tuple = tuple(x for x in tup if not (x == element and not found and (found := True)))
    return new_tuple

# Example usage
my_tuple = (1, 2, 3, 2, 4, 2, 5)
element_to_remove = 2

new_tuple = remove_first_occurrence(my_tuple, element_to_remove)
print(new_tuple)  # Output: (1, 3, 2, 4, 2, 5)