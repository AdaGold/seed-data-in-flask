from app import db
from app.models.simple_book import SimpleBook
from flask import Blueprint, jsonify, make_response, request

bp = Blueprint("simple_books", __name__, url_prefix="/simple_books")

@bp.route("/", methods=["POST"])
def create():
    request_body = request.get_json()
    new_book = SimpleBook.from_dict(request_body)

    db.session.add(new_book)
    db.session.commit()

    # note: without jsonify this returns text/html
    return jsonify(f"Book {new_book.title} successfully created"), 201

@bp.route("/", methods=["GET"])
def index():
    books = SimpleBook.query.all()
    books_response = [book.to_dict() for book in books]
    return jsonify(books_response)
