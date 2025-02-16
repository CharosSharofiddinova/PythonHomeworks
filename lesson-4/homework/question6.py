#Prime Numbers Task: Write a Python program that prints all prime numbers between 1 and 100.

def is_prime(n):
    """Checks if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to √n
        if n % i == 0:
            return False
    return True

# ✅ Print all prime numbers between 1 and 100
print("Prime numbers between 1 and 100:")
for num in range(1, 101):  # Loop through numbers 1 to 100
    if is_prime(num):
        print(num, end=" ")  # Print primes on the same line