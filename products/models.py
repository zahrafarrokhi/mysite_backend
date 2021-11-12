from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=15)
    image = models.ImageField(upload_to="Products_image/")
    price = models.IntegerField()
    active = models.BooleanField(default=False)
    quantity = models.IntegerField()


    def __str__(self):
        return f"{self.name} "
