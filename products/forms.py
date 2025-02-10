from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('Авто', 'Авто'),
        ('Електроніка', 'Електроніка'),
        ('Дім і сад', 'Дім і сад'),
        ('Одяг', 'Одяг'),
        ('Нерухомість', 'Нерухомість'),
        ('Дитячий світ', 'Дитячий світ'),
        ('Для геймерів', 'Для геймерів'),
        ('Інше', 'Інше'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label="Category")

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'image']
