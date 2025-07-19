from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='books'),
    path('library/', views.LibraryDetail.as_view(), name='library_detail')
]
