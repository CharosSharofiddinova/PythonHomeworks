#Create Nested Tuple: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.

def create_nested_tuple(tup, size):
    return tuple(tup[i:i+size] for i in range(0, len(tup), size))

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
size = 2  
nested_tuple = create_nested_tuple(my_tuple, size)
print(nested_tuple)  