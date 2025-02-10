#Write a program to check if a string contains any digits.

word_string = input("Enter a string: ")
if any(char.isdigit() for char in word_string):
     print("The string contains digits.")
else:
    print("The string does not contain any digits.")
   