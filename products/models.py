from django.db import models
from django.contrib.auth.models import User  
from django.core.validators import MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def str(self):
        return self.name

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Авто', 'Авто'),
        ('Електроніка', 'Електроніка'),
        ('Дім сад', 'Дім сад'),
        ('Одяг', 'Одяг'),
        ('Нерухомість', 'Нерухомість'),
        ('Дитячий світ', 'Дитячий світ'),
        ('Тварини', 'Тварини'),
        ('Інше', 'Інше'),
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    description = models.TextField()
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES)  
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(User, related_name='favorite_products', blank=True)

    def str(self):
        return f"{self.name} - {self.author.username}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='site_images/ava1.png', blank=True, null=True)

    def __str__(self):
        return self.user.username