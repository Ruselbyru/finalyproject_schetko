# Generated by Django 3.2.5 on 2021-07-04 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoprequest', '0003_alter_shoprequest_shopnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoprequest',
            name='firstname_lastname',
            field=models.CharField(max_length=100, verbose_name='Имя и фамилия владельца'),
        ),
        migrations.AlterField(
            model_name='shoprequest',
            name='shopemail',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='shoprequest',
            name='shopname',
            field=models.CharField(max_length=100, verbose_name='Наименование магазина'),
        ),
        migrations.AlterField(
            model_name='shoprequest',
            name='shopnumber',
            field=models.CharField(max_length=13, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='shoprequest',
            name='shopunp',
            field=models.CharField(max_length=9, verbose_name='УНП'),
        ),
    ]