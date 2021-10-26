from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    @classmethod
    def from_dict(cls, values):
        return cls(**values)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description
        }
