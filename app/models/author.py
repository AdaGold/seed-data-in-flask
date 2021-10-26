from app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    books = db.relationship("Book", backref="author")

    @classmethod
    def from_dict(cls, values):
        return cls(**values)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description
        }
