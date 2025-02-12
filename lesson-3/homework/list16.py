#Count Odd Numbers: Given a list of integers, count how many of them are odd

numbers = [4, 3, 2, 6, 7, 4, 8, 10]  # Example list of integers

odd_numbers = sum(1 for num in numbers if num % 2 == 1)  # Count even numbers
print("Count of odd numbers:", odd_numbers)