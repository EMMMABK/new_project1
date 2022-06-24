from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.forms import CharField

# Create your models here.
class Category(models.Model):
    name  = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=1000)
    description = models.TextField(blank=True)    
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    image = models.ImageField(upload_to='products', null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=1000)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="reviews") 

    def __str__(self):
        return self.text