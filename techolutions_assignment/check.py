import book  # Import the book module
import datetime

checkouts = []

def checkout_book(user_id: int, isbn: str) -> None:
    """
    Check out a book for a user.
    
    Parameters:
    - user_id (int): The ID of the user checking out the book.
    - isbn (str): The ISBN of the book to check out.
    
    Returns:
    - None
    """
    for b in book.books:
        if b["isbn"] == isbn:
            if not b.get("checked_out", False):
                b["checked_out"] = True
                timestamp = datetime.datetime.now()
                checkouts.append({"user_id": user_id, "isbn": isbn, "timestamp": timestamp})
                print(f"User {user_id} successfully checked out book '{b['title']}' (ISBN: {isbn}) at {timestamp}.")
                book.storage.save_to_file(book.BOOK_FILE, book.books)  # Save updated book list
            else:
                print(f"Book with ISBN {isbn} is already checked out.")
            return
    print(f"No book found with ISBN {isbn}.")
