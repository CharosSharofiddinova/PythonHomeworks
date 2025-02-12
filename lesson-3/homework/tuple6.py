#Last Element: Access the last element of a tuple, considering what to return if the tuple is empty.
def get_last_element(tup):
    return tup[-1] if tup else None  

# Example usage:
my_tuple = (3, 7, 1, 9)
empty_tuple = ()

print(get_last_element(my_tuple))   # Output: 9
print(get_last_element(empty_tuple))  # Output: None