#First Element: Access the first element of a list, considering what to return if the list is empty

numbers=[1,3,5,7,9,11,13] #list numbers
if numbers:
    first_element=numbers[0]
    print("The first element is ", first_element)
else:
    print("The list is empty")    