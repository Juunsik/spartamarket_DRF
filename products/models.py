from django.db import models
from django.conf import settings


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    image = models.ImageField(default="product/choonsik.jpg", upload_to="product")
    author = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
