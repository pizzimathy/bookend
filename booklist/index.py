#!/usr/bin/env python3

import os
import os.path as p
import booklist.files as f
import argparse

from json import dumps
from booklist.book import BookEncoder, Book

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "lists.json")


def init(args):

    # no lists exist -> make a new list
    if not p.isfile(path):

        print("You don't have any booklists!")

        f.makefile(path)

        books = {
            "books": []
        }

        f.write(dumps(books))

        if args.add:
            book = Book()
            BookEncoder.encode(book.__dict__)

    elif args.search:

        decoder = BookEncoder()
        decoder.decode()
        results = []

        for book in decoder.collection:

            s = args.search.lower()

            if s in book["title"].lower():
                results.append(Book.formatbook(book, "title"))
            elif s in book["author"].lower():
                results.append(Book.formatbook(book, "author"))
            elif s in book["booklist"].lower():
                results.append(Book.formatbook(book, "booklist"))

        for book in results:
            print(book)

    elif args.add:

        book = Book()
        BookEncoder.encode(book.__dict__)

    elif args.list:

        decoder = BookEncoder()
        decoder.decode()

        for book in decoder.collection:
            print(Book.formatbook(book))

    elif args.checkout:

        decoder = BookEncoder()
        decoder.remove(args.checkout)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--search", help="'-s <term>' to search for a term across all lists")
    parser.add_argument("-l", "--list", help="prints a list of booklists", action="store_true")
    parser.add_argument("-a", "--add", help="add a new book!", action="store_true")
    parser.add_argument("-c", "--checkout", help="enter the title of a book, and it'll be removed from the list")
    parsed = parser.parse_args()

    init(parsed)
