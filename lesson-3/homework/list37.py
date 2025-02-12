#Sum of Negative Numbers: Given a list of numbers, calculate the sum of all negative numbers.

numbers=[-2,-4,-3,5,6,7,8,1]
negative_numbers= [num for num in numbers if num<0]
total_sum=sum(negative_numbers)
print(total_sum)