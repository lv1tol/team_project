from django import forms
from .models import Product
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('Авто', 'Авто'),
        ('Електроніка', 'Електроніка'),
        ('Дім і сад', 'Дім і сад'),
        ('Одяг', 'Одяг'),
        ('Нерухомість', 'Нерухомість'),
        ('Дитячий світ', 'Дитячий світ'),
        ('Тварини', 'Тварини'),
        ('Інше', 'Інше'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label="Category")

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'image']

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data