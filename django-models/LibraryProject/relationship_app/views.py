from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile




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


class LoginView(FormView):
    template_name = 'relationship_app/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')  # Change 'home' to your desired redirect URL name

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)
    

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # or any URL name you've set
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


class RegisterView(FormView):
    template_name = 'relationship_app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')  # Redirect after successful registration

    def form_valid(self, form):
        user = form.save()            # Save the new user
        login(self.request, user)     # Log the user in immediately
        return super().form_valid(form)
    


# Helpers for role checks
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')