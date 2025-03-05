def find_factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")

# Get user input
num = int(input("Enter a positive integer: "))

# Validate input
if num > 0:
    find_factors(num)
else:
    print("Please enter a positive integer.")
