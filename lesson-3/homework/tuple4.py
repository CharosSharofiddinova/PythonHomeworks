#Check Element: Given a tuple and an element, check if the element is present in the tuple.
def check_element(tup, element):
    return element in tup
my_tuple = (10, 20, 30, 40, 50)
element_to_check = 30
print(check_element(my_tuple, element_to_check))