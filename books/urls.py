# books/urls.py
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookUpdateView,
    BookCreateView,
    BookDeleteView
)

app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('edit/<int:pk>/', BookUpdateView.as_view(), name='book_edit'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
]
