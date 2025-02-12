#Find Minimum of Subtuple: Given a tuple, find the minimum element of a specified subtuple.
def min_of_subtuple(tup, start, end):
    subtuple = tup[start:end]  # Slice the tuple
    return min(subtuple) if subtuple else None  # Return max or None if empty

my_tuple = (3, 1, 7, 9, 2, 8)
start_index = 5
end_index = 1  # Slicing goes up to index 5 (excluding 5)

max_value = min_of_subtuple(my_tuple, end_index, start_index)
print(max_value)  # Output: 9 