from app import create_app
from app.seed.book import load_from_csv

my_app = create_app()
with my_app.app_context():
    load_from_csv()