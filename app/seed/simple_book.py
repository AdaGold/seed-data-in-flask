import csv
from app import db
from app.models.simple_book import SimpleBook

def make_100():
    for i in range(100):
        id = i + 1
        title = f"Book {id}"
        description = f"Description {id}"
        record = SimpleBook(title=title, description=description)
        db.session.add(record)

    db.session.commit()

def load_from_csv():
    with open("data/simple_book.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # title = row["title"]
            # description = row["description"]
            record = SimpleBook.from_dict(row)
            db.session.add(record)

        db.session.commit()
        
