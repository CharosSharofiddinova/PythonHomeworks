#Get Unique Elements in Order: Given a list, create a new list that 
# contains unique elements while maintaining the original order

def get_unique_elements(lst):
    seen = set()
    return [x for x in lst if x not in seen and not seen.add(x)]

# Example usage
numbers = [3, 1, 2, 3, 4, 2, 5, 1, 6]
print(get_unique_elements(numbers))  
# Output: [3, 1, 2, 4, 5, 6]