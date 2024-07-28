from django.db import models

# Create your models here.

class AttributeName(models.Model):
    id = models.AutoField(primary_key=True)
    nazev = models.CharField(max_length=50, blank=True)
    kod = models.CharField(max_length=50, blank=True)
    zobrazit = models.BooleanField(default=False)


class AttributeValue(models.Model):
    id = models.AutoField(primary_key=True)
    hodnota = models.CharField(max_length=100)


class Attribute(models.Model):
    id = models.AutoField(primary_key=True)
    nazev_atributu_id = models.ForeignKey(
        AttributeName, on_delete=models.CASCADE)
    hodnota_atributu_id = models.ForeignKey(
        AttributeValue, on_delete=models.CASCADE)
    
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    obrazek = models.URLField()
    nazev = models.CharField(max_length=100, blank=True)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    nazev = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    mena = models.CharField(max_length=10, blank=True)
    published_on = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)


class ProductAttributes(models.Model):
    id = models.AutoField(primary_key=True)
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductImage(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    obrazek_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    nazev = models.CharField(max_length=250)


class Catalog(models.Model):
    id = models.AutoField(primary_key=True)
    nazev = models.CharField(max_length=250, blank=True)
    obrazek_id = models.ForeignKey(Image, null=True, on_delete=models.SET_NULL)
    products_ids = models.ManyToManyField(Product, blank=True)
    attributes_ids = models.ManyToManyField(Attribute, blank=True)