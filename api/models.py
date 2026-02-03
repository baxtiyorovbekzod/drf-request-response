from django.db import models


class Item(models.Model):
    name = models.CharField()
    desc = models.TextField()
    category = models.CharField()
    price = models.FloatField()
    is_active = models.BooleanField()


class Product(models.Model):
    name = models.CharField()
    desc = models.TextField()
    category = models.CharField()
    price = models.FloatField()
    is_active = models.BooleanField()
    stock = models.PositiveIntegerField()

# GET api/products
# POST api/products
# GET api/products/id
# PUT api/products/id
# DELETE api/products/id
