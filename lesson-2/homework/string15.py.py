#Ask the user for a sentence and create an acronym from the first letters of each word.
#Example:
#Input: "World Health Organization"
#Output: "WHO"

sentance=input("Input a sentance: ")
words = sentance.split()
acronym=''.join([word[0].upper() for word in words])
print(acronym)
