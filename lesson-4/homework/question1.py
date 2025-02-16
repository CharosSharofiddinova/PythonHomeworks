#Return uncommon elements of lists. Order of elements does not matter.

def find_uncommon_elements(list1, list2):
    return list(set(list1) ^ set(list2))  

list1 = [1, 1, 2]
list2 = [2, 3, 4]

print(find_uncommon_elements(list1, list2))  

#second example
def find_uncommon_elements(list1, list2):
    return list(set(list1) ^ set(list2))  

list_numbers1 = [1, 2, 3]
list_numbers2 = [4, 5, 6]

print(find_uncommon_elements(list_numbers1, list_numbers2))  

