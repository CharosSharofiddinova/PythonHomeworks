#Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.
#Example:
#Input sentence: "I love apples."
#Replace: "apples"
#With: "oranges"
#Output: "I love oranges."

sentence = input("Write a sentence: ")
word_to_replace = input("write the word to replace: ")
replacement_word = input("Write the replacement word: ")
new_sentence = sentence.replace(word_to_replace, replacement_word)
print("Updated sentence:", new_sentence)