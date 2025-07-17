from relationship_app.models import Author, Book, Library

library_name = ''
author_name = ''

library = Library.objects.get(name=library_name)
books = library.books.all()

author = Author.objects.get(name=author_name)
book = Book.objects.filter(author=author)

librarian = library.librarian