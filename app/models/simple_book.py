from app import db

class SimpleBook(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    @classmethod
    def from_dict(cls, values):
        return cls(**values)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description
        }
