#Create Range List: Create a list of numbers in a specified range (e.g., from 1 to 10).uu

def create_range_list(start, end, step=1):

    return list(range(start, end + 1, step))

# Example usage
print(create_range_list(1, 10))  
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(create_range_list(1, 10, 2))  
# Output: [1, 3, 5, 7, 9]