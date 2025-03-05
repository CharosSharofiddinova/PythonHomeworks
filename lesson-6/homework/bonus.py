import os
import string
from collections import Counter

def get_text(filename="sample.txt"):
    """Reads text from the file or prompts the user to create it if it doesn't exist."""
    if not os.path.exists(filename):
        text = input("File not found. Enter a paragraph to create 'sample.txt': ")
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
        return text

    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def count_words(text):
    """Counts the frequency of words, ignoring case and punctuation."""
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return Counter(words)

def save_report(word_counts, top_n, output_file="word_count_report.txt"):
    """Saves the word frequency report to a file."""
    total_words = sum(word_counts.values())
    top_words = word_counts.most_common(top_n)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("Word Frequency Report\n")
        file.write(f"Total Words: {total_words}\n\n")
        file.write(f"Top {top_n} Words:\n")
        for word, count in top_words:
            file.write(f"{word} - {count}\n")

    print(f"\nReport saved to '{output_file}'.")

def main():
    text = get_text()
    word_counts = count_words(text)

    while True:
        try:
            top_n = int(input("Enter the number of top common words to display: "))
            if top_n <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    total_words = sum(word_counts.values())
    top_words = word_counts.most_common(top_n)

    print(f"\nTotal words: {total_words}")
    print(f"Top {top_n} most common words:")
    for word, count in top_words:
        print(f"{word} - {count} times")

    save_report(word_counts, top_n)

if __name__ == "__main__":
    main()
