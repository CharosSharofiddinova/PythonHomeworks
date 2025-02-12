#Count Occurrences: Given a tuple and an element, find how many times the element appears in the tuple
def count_occurrences(tup, element):
    return tup.count(element)

# Example usage:
my_tuple = (1, 2, 3, 4, 2, 2, 5, 6, 2)
element_to_count = 2
print(count_occurrences(my_tuple, element_to_count))  