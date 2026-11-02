from django.views.generic import ListView

from library.models import Book


class BookListView(ListView):
    model = Book