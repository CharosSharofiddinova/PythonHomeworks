#Filter Even Numbers: Given a list of integers, create a new list that contains only the even numbers.

list_numbers=[2,4,5,7,8,11,12]
even_list= [num for num in list_numbers if num % 2 == 0]
print("List of even numbers: ", even_list)
