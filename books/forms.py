from .models import Book
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class EditBook(ModelForm):
    
    class Meta:
        # the Model from which the form will inherit from
        model = Book
        # the fields we want from the Model
        fields = '__all__'
        # styling the form with bootstrap classes
        widgets = {
             'title': forms.TextInput(attrs={'class': 'form-control'}),
             'author': forms.TextInput(attrs={'class': 'form-control'}),
             'price': forms.TextInput(attrs={'class': 'form-control'}),
             'isbn': forms.TextInput(attrs={'class': 'form-control'}),
             'image': forms.TextInput(attrs={'class': 'form-control'}),
             'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']