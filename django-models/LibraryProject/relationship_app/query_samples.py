from relationship_app.models import Book, Library

library_name = ''
author_name = ''

library = Library.objects.get(name=library_name)
books = library.books.all()

book = Book.objects.get(author__name=author_name)

librarian = library.librarian