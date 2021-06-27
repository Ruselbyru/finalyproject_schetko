from django.db import models
from django.urls import reverse

# Create your models here.

class Shoprequest (models.Model):
    shopname = models.CharField(max_length=100)
    firstname_lastname = models.CharField(max_length=100)
    shopnumber = models.CharField(max_length=13)
    shopemail = models.EmailField()
    shopunp = models.CharField (max_length=9)

    def __str__(self):
        return self.shopname

    def get_absolute_url (self):
        return reverse('shoprequest')
