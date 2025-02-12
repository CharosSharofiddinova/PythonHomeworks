#Check Palindrome: Given a list, check if the list is a palindrome (reads the same forwards and backwards).

def is_palindrome(words):
    return words==words[::-1]
print(is_palindrome([1,2,3,3,2,1]))
print(is_palindrome([1,23,4,5, 3,2,1]))