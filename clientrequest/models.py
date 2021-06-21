from django.db import models

# Create your models here.
class BrandAuto (models.Model):
    brand_auto = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_auto


class ModelAuto (models.Model):
    model_auto = models.ForeignKey(BrandAuto,on_delete=models.CASCADE)

    def __str__(self):
        return self.model_auto