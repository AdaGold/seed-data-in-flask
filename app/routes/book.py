from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request

bp = Blueprint("books", __name__, url_prefix="/books")

@bp.route("/", methods=["GET"])
def index():
    books = Book.query.all()
    books_response = [book.to_dict() for book in books]
    return jsonify(books_response)
