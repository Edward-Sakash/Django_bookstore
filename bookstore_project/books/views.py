from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'book_list'
    
    def get(self, request, *args, **kwargs):
        books_queryset = self.get_queryset()
        books_list = list(books_queryset)
        print(books_list)

        return super().get(request, *args, **kwargs)

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'author', 'description', 'published_date', 'price']

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'author', 'description', 'published_date', 'price']

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('books:book_list')

