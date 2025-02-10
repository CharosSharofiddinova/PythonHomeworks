#Write a Python program to:
#Take a string input from the user.
#Print the length of the string.
#Convert the string to uppercase and lowercase.

word=input("Type a word: ")
lower_case=word.lower()
upper_case=word.upper()
print(f"The length is: {len(word)}\nThe lowercase: {lower_case}\nThe uppercase: {upper_case}")