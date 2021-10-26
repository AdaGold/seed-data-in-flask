import csv
from app import db
from app.models.book import Book
from app.models.author import Author
from random import randint

def load_from_csv():
    authors = {}

    with open("data/author.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            author_id = row.pop("seed_id")
            author = Author.from_dict(row)
            authors[author_id] = author
            db.session.add(author)

        db.session.commit()
        
    with open("data/book.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            book_id = row.pop("seed_id")
            seed_author_id = row.pop("seed_author_id")
            book = Book.from_dict(row)
            book.author = authors[seed_author_id]
            db.session.add(book)

        db.session.commit()
        

def make_20_authors():
    for i in range(20):
        id = i + 1
        name = f"Author {id}"
        author = Author(name=name)
        db.session.add(author)
        db.session.commit()

        num_books = randint(0, 5)
        for j in range(num_books):
            id = j + 1
            title = f"Book {id} by {name}"
            description = f"Description {id}"
            book = Book(title=title, description=description)
            book.author = author
            db.session.add(book)

        db.session.commit()

