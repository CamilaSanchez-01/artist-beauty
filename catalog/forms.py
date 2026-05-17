from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Artist, Product, Category, Review


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={
                'rows': 3, 'class': 'form-control',
                'placeholder': '¿Qué te pareció este producto?'}),
        }


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'brand_name', 'bio', 'image_url',
                  'iconic_song_title', 'iconic_song_url', 'iconic_song_lyrics']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand_name': forms.TextInput(attrs={'class': 'form-control'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
            'iconic_song_title': forms.TextInput(attrs={'class': 'form-control'}),
            'iconic_song_url': forms.URLInput(attrs={'class': 'form-control'}),
            'iconic_song_lyrics': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['artist', 'category', 'name', 'description', 'price',
                  'image_url', 'rating', 'is_bestseller', 'stock']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'artist': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': 0, 'max': 5}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        }
