from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'description', 'published_date', 'price']

class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'description', 'published_date', 'price']

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('books:book_list')
