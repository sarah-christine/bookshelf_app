from flask import Flask, render_template
from database.db import create_books_table

app = Flask(__name__)

create_books_table() # Ensure the books table exists, runs once on startup

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
