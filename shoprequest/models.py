from django.db import models
from django.urls import reverse


# Create your models here.
#Модель БД для Магазинов с полями : Наименование, Владелец, Номер, Почта, УНП
class Shoprequest (models.Model):
    shopname = models.CharField(verbose_name='Наименование магазина', max_length=100)
    firstname_lastname = models.CharField(verbose_name='Имя и фамилия владельца', max_length=100)
    shopnumber = models.CharField(verbose_name='Телефон', max_length=13)
    shopemail = models.EmailField(verbose_name='Email', )
    shopunp = models.CharField (verbose_name='УНП', max_length=9)

    def __str__(self):
        return self.shopname

    def get_absolute_url (self):
        return reverse('goodshop')

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'