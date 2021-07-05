from django.db import models
from shoprequest.models import Shoprequest


# Create your models here.
#Модель БД для записи пользователей ботом с полями : Имя магазина, ид в телеграмме, статус подписки
class Shop_telegram (models.Model):
    shopname = models.OneToOneField(Shoprequest, on_delete=models.CASCADE)
    telegram_id = models.CharField(max_length=9)
    subscribe = models.BooleanField(null=True)

    def __str__(self):
        return self.telegram_id

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'