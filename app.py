from flask import Flask, render_template, request, redirect, url_for
from database.db import create_books_table, get_connection, add_book, get_all_books

app = Flask(__name__)

create_books_table() # Ensure the books table exists, runs once on startup

# TEMP: add some test books - to be removed later
add_book("1984", "George Orwell")
add_book("To Kill a Mockingbird", "Harper Lee")

@app.route('/')
def home():
    books = get_all_books()
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    author = request.form['author']

    add_book(title, author)

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)