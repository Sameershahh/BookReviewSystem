from django import forms
from .models import Book

class formBook(forms.ModelForm):
    
    class Meta:
        model =  Book
        fields = ("title",'author','isbn','genre','publication_date','rating')