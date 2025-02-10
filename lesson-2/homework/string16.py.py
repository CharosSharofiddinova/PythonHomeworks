#Write a program that asks the user for a string and a character, 
#then removes all occurrences of that character from the string.

word_string = input("Enter a string: ")
char_to_remove = input("Enter the character to remove: ")
new_string = word_string.replace(char_to_remove, "")
print("Updated string:", new_string)