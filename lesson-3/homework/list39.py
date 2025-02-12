def create_nested_list (numbers, size):
    return [numbers[i:i+size] for i in range(0, len(numbers), size)]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sublist_size = 3
print(create_nested_list(numbers, sublist_size))  
