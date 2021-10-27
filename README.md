# Seed Data in Flask

## About

This repository has models and migrations already created for a simple book (no cross-table relationships), as well as a book that has an external relationship to an author.

Because the migrations have been created already, there's no need to run the initialization or migration steps for flask db. Instead, we need only run
```bash
createdb -U postgres seed_data_development
flask db upgrade
```

We can drop and recreate the database as desired with
```bash
dropdb seed_data_development
createdb -U postgres seed_data_development
flask db upgrade
```

A completed implementation is available in the `seed-data` branch, where modules containing seed methods are found under the `app/seed` directory, which can be loaded from the `flask shell`. Alternatively, small wrapper scripts can be found in the project root, and can be run as normal with `python seed_book.py` or `python seed_simple_book.py`.

Review the videos for this session for additional details.