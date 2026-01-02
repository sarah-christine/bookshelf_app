import sqlite3

DB_PATH = 'database/bookshelf.db'

def get_connection():
    return sqlite3.connect(DB_PATH)

# Create the books table if it doesn't exist
def create_books_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            read INTEGER DEFAULT 0,
            liked INTEGER DEFAULT 0,
            UNIQUE (title, author)
        )
    ''')
    conn.commit()
    conn.close()

# Add a new book to the books table
def add_book(title, author):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        # Handles duplicate titles
        return False
    
# Retrieve all books from the books table
def get_all_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return books