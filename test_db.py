# Temporary test code
from database.db import add_book, get_all_books
add_book("The Great Gatsby", "F. Scott Fitzgerald")
add_book("The Great Gatsby", "F. Scott Fitzgerald")  # Duplicate, should be handled
print(get_all_books())