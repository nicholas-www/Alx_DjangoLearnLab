from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from .models import Library, Book

# Create your views here.

def list_books(request):
    books = Book.objects.all()

    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(ListView):
    template_name = 'relationship_app/library_detail.html'
    model = Library
    context_object_name = 'libraries'


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

    return render(request, 'relationship_app/login.html')