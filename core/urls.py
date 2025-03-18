from django.urls import path
from core import views
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/add/', BookCreateView.as_view(), name='add_book'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='edit_book'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='delete_book'),
]