#Get All Indices of Element: Given a tuple and an element, find all the indices of that element in the tuple.
def get_all_indices(tup, element):
    return [index for index, value in enumerate(tup) if value == element]

my_tuple = (1, 2, 3, 2, 4, 2, 5)
element_to_find = 2

indices = get_all_indices(my_tuple, element_to_find)
print(indices)  