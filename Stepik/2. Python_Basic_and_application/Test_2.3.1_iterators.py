books = {
    'title': 'The langoliers',
    'author': 'Stephen King',
    'year published': 1990
}

books_iterator = iter(books)
print(next(books_iterator))

books_it = iter(books)
while True:
    try:
        print(next(books_it))
    except StopIteration:
        break
