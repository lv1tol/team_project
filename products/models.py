from django.db import models

class Product(models.Model):
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

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES)  
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name
