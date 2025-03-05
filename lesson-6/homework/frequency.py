import os
import string
from collections import Counter

def get_text():
    """Reads text from sample.txt or creates the file if not found."""
    if not os.path.exists("sample.txt"):
        text = input("Enter a paragraph to save in sample.txt: ")
        with open("sample.txt", "w") as file:
            file.write(text)
    else:
        with open("sample.txt", "r") as file:
            text = file.read()
    return text

def count_words(text):
    """Counts the frequency of words in the given text."""
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return Counter(words)

def save_report(word_counts):
    """Saves the word frequency report to word_count_report.txt."""
    total_words = sum(word_counts.values())
    top_words = word_counts.most_common(5)
    
    with open("word_count_report.txt", "w") as file:
        file.write(f"Total Words: {total_words}\n")
        file.write("Top 5 Words:\n")
        for word, count in top_words:
            file.write(f"{word} - {count}\n")

def main():
    text = get_text()
    word_counts = count_words(text)
    save_report(word_counts)
    
    print(f"Total words: {sum(word_counts.values())}")
    print("Top 5 most common words:")
    for word, count in word_counts.most_common(5):
        print(f"{word} - {count} times")

if __name__ == "__main__":
    main()
