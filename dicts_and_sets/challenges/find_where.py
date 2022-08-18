# Реализуйте функцию find_where(), которая принимает на вход список книг и
# поисковый запрос и возвращает первую книгу, которая соответствует запросу.
# Каждая книга в списке — это словарь, содержащий её параметры, поисковый
# запрос — тоже словарь с параметрами.
# Если совпадений не было, то функция должна вернуть None.


def find_where(books: list[dict], requested_book):
    found = False
    if not requested_book:
        return books[0]
    for catalog_index, book_in_catalog in enumerate(books):
        for category in requested_book:
            if (
                requested_book.get(category, None) ==
                book_in_catalog.get(category, None) and
                category in books[0]
            ):
                found = True
            else:
                found = False
                break
        if found:
            return books[catalog_index]


TITLE, AUTHOR, YEAR = 'title', 'author', 'year'
BOOKS = [
    {TITLE: 'Book of Fooos', AUTHOR: 'Foo', YEAR: 1111},
    {TITLE: 'Cymbeline', AUTHOR: 'Shakespeare', YEAR: 1611},
    {TITLE: 'The Tempest', AUTHOR: 'Shakespeare', YEAR: 1611},
    {TITLE: 'Book of Foos Barrrs', AUTHOR: 'FooBar', YEAR: 2222},
    {TITLE: 'Still foooing', AUTHOR: 'FooBar', YEAR: 333},
    {TITLE: 'Happy Foo', AUTHOR: 'FooBar', YEAR: 4444},
]
assert find_where(BOOKS, {}) == BOOKS[0]
assert find_where(BOOKS, {AUTHOR: 'Pushkin'}) is None
assert find_where(BOOKS, {YEAR: 1111, AUTHOR: 'Pushkin'}) is None
assert find_where(BOOKS, {"genre": None}) is None
assert find_where(
    BOOKS, {YEAR: 1111},
) == {TITLE: 'Book of Fooos', AUTHOR: 'Foo', YEAR: 1111}
assert find_where(
    BOOKS, {AUTHOR: 'Shakespeare', YEAR: 1611},
)[TITLE] == 'Cymbeline'
assert find_where(BOOKS, BOOKS[2]) == BOOKS[2]
