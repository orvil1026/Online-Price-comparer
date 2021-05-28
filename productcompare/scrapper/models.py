from django.db import models


class Product(models.Model):

    name=models.CharField(max_length=300)
    title=models.CharField(max_length=300)
    price=models.CharField(max_length=300)
    rating=models.CharField(max_length=300)
    image_url=models.URLField(max_length=300)
    url=models.URLField(max_length=300)
    website=models.CharField(max_length=300)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

# Create your models here.
