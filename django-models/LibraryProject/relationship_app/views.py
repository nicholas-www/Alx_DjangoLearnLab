from django.shortcuts import render
from django.views.generic import ListView

from .models import Library, Book

# Create your views here.

def list_books(request):
    books = Book.objects.all()

    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetail(ListView):
    template_name = 'relationship_app/library_detail.html'
    model = Library
    context_object_name = 'libraries'