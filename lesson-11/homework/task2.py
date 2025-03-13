import sqlite3

# Step 1: Create a new SQLite database and define the Books table
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
""")

books = [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
]
cursor.executemany("INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)", books)
conn.commit()

cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")
conn.commit()
cursor.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
dystopian_books = cursor.fetchall()
print("Dystopian Books:")
for book in dystopian_books:
    print(book)
cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")
conn.commit()
cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
conn.commit()
ratings = {
    "To Kill a Mockingbird": 4.8,
    "1984": 4.7,
    "The Great Gatsby": 4.5
}
for title, rating in ratings.items():
    cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (rating, title))
conn.commit()
cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
sorted_books = cursor.fetchall()
print("\nBooks sorted by Year Published:")
for book in sorted_books:
    print(book)

conn.close()
