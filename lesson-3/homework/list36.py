#Sum of Positive Numbers: Given a list of numbers, calculate the sum of all positive numbers.

numbers=[-2,-4,3,5,6,7,8,1]
positive_numbers= [num for num in numbers if num>0]
total_sum=sum(positive_numbers)
print(total_sum)