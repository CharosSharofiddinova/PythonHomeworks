#Find Maximum of Subtuple: Given a tuple, find the maximum element of a specified subtuple.
def max_of_subtuple(tup, start, end):
    subtuple = tup[start:end]  # Slice the tuple
    return max(subtuple) if subtuple else None  # Return max or None if empty

my_tuple = (3, 1, 7, 9, 2, 8)
start_index = 1
end_index = 5  # Slicing goes up to index 5 (excluding 5)

max_value = max_of_subtuple(my_tuple, start_index, end_index)
print(max_value)  # Output: 9