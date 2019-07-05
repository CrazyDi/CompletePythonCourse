import json
import os.path


"""
Concerned with storing and retrieving books from a list.
"""


def read_from_file():
    books = []
    if os.path.exists('books.json'):
        with open('books.json', 'r') as file:
            books = json.load(file)

    return books


def write_to_file(books):
    with open('books.json', 'w') as file:
        json.dump(books, file)


def add_book(name, author):
    books = read_from_file()

    books.append({'name': name, 'author': author, 'read': False})

    write_to_file(books)


def get_all_books():
    return read_from_file()


def mark_book_as_read(name):
    books = read_from_file()

    for book in books:
        if book['name'] == name:
            book['read'] = True

    write_to_file(books)


def delete_book(name):
    books = read_from_file()
    books = [book for book in books if book['name'] != name]
    write_to_file(books)
