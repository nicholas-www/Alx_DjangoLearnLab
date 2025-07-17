from relationship_app.models import Book, Library

library = Library.objects.get(name='Library')
books = library.books.all()

book = Book.objects.get(author__name='George Orwell')

librarian = library.librarian