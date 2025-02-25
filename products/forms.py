from django import forms
from .models import Product, Profile
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('Auto', 'Auto'),
        ('Electronics', 'Electronics'),
        ('Home/Garden', 'Home/Garden'),
        ('Clothes', 'Clothes'),
        ('Realty', 'Realty'),
        ('Toys', 'Toys'),
        ('Animals', 'Animals'),
        ('Other', 'Other'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label="Category")

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'image']

class RegisterForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Цей email уже використовується.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile, created = Profile.objects.get_or_create(user=user)  # Виправлено
            if 'avatar' in self.cleaned_data:
                profile.avatar = self.cleaned_data['avatar']
                profile.save()
        return user