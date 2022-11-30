from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator


# Create your models here.
class Catagories(models.Model):

    catagory_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.catagory_name

class Products(models.Model):
    product_name=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)
    catagory=models.ForeignKey(Catagories,on_delete=models.CASCADE)
    description=models.CharField(max_length=100)


    def __str__(self):
        return self.product_name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("in-cart","in-cart"),
        ("pending","pending"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=100,choices=options,default="in-cart")

class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    comment=models.CharField(max_length=100)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together=["user","product"]