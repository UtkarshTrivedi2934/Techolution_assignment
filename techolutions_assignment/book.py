import storage  # Handles file-based storage
import os

BOOK_FILE = 'books.json'
books = storage.load_from_file(BOOK_FILE)

def add_book(title: str, author: str, isbn: str) -> None:
    """
    Add a new book to the system and save to file.
    """
    if any(book["isbn"] == isbn for book in books):
        print(f"ISBN {isbn} already exists. Please use a unique ISBN.")
        return

    books.append({"title": title, "author": author, "isbn": isbn})
    storage.save_to_file(BOOK_FILE, books)
    print(f"Book '{title}' added successfully.")

def list_books() -> None:
    """
    List all books in the system.
    """
    if not books:
        print("No books available.")
        return
    for book in books:
        print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
