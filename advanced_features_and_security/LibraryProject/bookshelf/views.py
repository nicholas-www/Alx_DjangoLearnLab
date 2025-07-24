from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm

# Create your views here.

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    pass

def example_form(request):
    form = ExampleForm()

    context = {'form': form}
    return render(request, 'bookshelf/example_form.html', context)