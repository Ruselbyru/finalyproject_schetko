from django.db import models
from django.urls import reverse

# Create your models here.
class BrandAuto (models.Model):
    brand_auto = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_auto


class ModelAuto (models.Model):
    brandauto = models.ForeignKey(BrandAuto,on_delete=models.CASCADE)
    model_auto = models.CharField(max_length=50)

    def __str__(self):
        return self.model_auto


class ClientRequest (models.Model):
    client_name = models.CharField (verbose_name='Имя', max_length=30)
    brandauto = models.ForeignKey (BrandAuto, verbose_name='Марка автомобиля', on_delete=models.CASCADE)
    modelauto = models.ForeignKey (ModelAuto, verbose_name='Модель автомобиля', on_delete=models.CASCADE)
    year_auto = models.CharField (verbose_name='Год выпуска автомобиля', max_length=4)
    client_request = models.TextField (verbose_name='Запчасти')
    client_phone = models.CharField (verbose_name='Телефон', max_length=13)

    def __str__(self):
        return self.client_name

    def get_absolute_url (self):
        return reverse('home')