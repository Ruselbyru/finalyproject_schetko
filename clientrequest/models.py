from django.db import models

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
    client_name = models.CharField (max_length=30)
    brandauto = models.OneToOneField (BrandAuto, on_delete=models.CASCADE)
    modelauto = models.OneToOneField (ModelAuto, on_delete=models.CASCADE)
    year_auto = models.CharField (max_length=4)
    client_request = models.TextField ()
    client_phone = models.CharField (max_length=13)

    def __str__(self):
        return self.client_name