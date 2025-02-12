#First Element: Access the first element of a tuple, considering what to return if the tuple is empty.

def get_first_element(tup):
    return tup[0] if tup else None  # Return None if the tuple is empty
my_tuple = (5, 10, 15)
empty_tuple = ()

print(get_first_element(my_tuple))   
print(get_first_element(empty_tuple))  