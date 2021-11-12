from django.db import models


class Contact(models.Model):
    subject = models.CharField(max_length=30)
    description = models.TextField()
    email = models.EmailField()

