# Generated by Django 3.2.4 on 2021-06-27 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoprequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.CharField(max_length=100)),
                ('firstname_lastname', models.CharField(max_length=100)),
                ('shopemail', models.EmailField(max_length=254)),
                ('shopunp', models.CharField(max_length=9)),
            ],
        ),
    ]
