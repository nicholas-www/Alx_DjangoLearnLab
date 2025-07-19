from django.urls import path
from .views import LibraryDetailView, list_books

urlpatterns = [
    path('books/', list_books, name='books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail')
]
