from django.shortcuts import render
from django.views import generic
from .models import *


class IndexView(generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.order_by('-publication_date')


class BookView(generic.DetailView):
    model = Book
    template_name = 'books/book.html'


class AuthorView(generic.DetailView):
    template_name = 'books/author.html'
    model = Author
