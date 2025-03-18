from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import formBook
from django.contrib import messages
from django.views.generic.base import TemplateView, RedirectView

# Home View
# def home(request):
#     form = formBook()
#     data = Book.objects.all()
#     return render(request, 'core/home.html',{'books':data,'form':form})

class home(TemplateView):
    template_name = 'core/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context


# Book List View
class BookListView(TemplateView):
    template_name = 'core/book_list.html'
    # context_object_name = 'books'

# Book Detail View
class BookDetailView(TemplateView):
    template_name = 'core/book_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        context['book'] = Book.objects.get(pk=pk)
        return context

# Book Create View
class BookCreateView(CreateView):
    def get(self, request):
        form = formBook()
        return render(request, 'core/book_form.html',{'form':form})
    
    def post(self, request):
        form = formBook(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Book Created Successfully!!')
            return redirect('add_book')
        return render(request, 'core/book_form.html',{'form':form})
    
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'core/book_form.html'  # Reuse the same form template for adding and editing
    fields = ['title', 'author', 'genre', 'publication_date', 'isbn',]
    success_url = reverse_lazy('book_list')  # Redirect to the book list after editing

# Delete Book View
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'core/book_confirm_delete.html'  # Template for delete confirmation
    success_url = reverse_lazy('book_list')  # Redirect to the book list after deletion