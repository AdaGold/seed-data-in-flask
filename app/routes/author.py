from app import db
from app.models.author import Author
from flask import Blueprint, jsonify, make_response, request

bp = Blueprint("author", __name__, url_prefix="/authors")

@bp.route("/", methods=["GET"])
def index():
    authors = Author.query.all()
    authors_response = [author.to_dict() for author in authors]
    return jsonify(authors_response)

@bp.route("/<id>/books", methods=["GET"])
def get_books(id):
    author = Author.query.get(id)
    books_response = [book.to_dict() for book in author.books]
    return jsonify(books_response)
