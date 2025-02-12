#Last Element: Access the last element of a list, considering what to return if the list is empty

numbers=[1,3,5,7,9,11,13] #list numbers
if numbers:
    last_element=numbers[-1]
    print("The last element is ", last_element)
else:
    print("The list is empty")    