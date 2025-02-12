#Count Even Numbers: Given a list of integers, count how many of them are even.

numbers = [4, 3, 2, 6, 7, 4, 8, 10]  # Example list of integers

even_numbers = sum(1 for num in numbers if num % 2 == 0)  # Count even numbers
print("Count of even numbers:", even_numbers)