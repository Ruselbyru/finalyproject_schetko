# Generated by Django 3.2.4 on 2021-06-21 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientrequest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=30)),
                ('year_auto', models.CharField(max_length=4)),
                ('client_request', models.TextField()),
                ('client_phone', models.CharField(max_length=13)),
                ('brandauto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clientrequest.brandauto')),
                ('modelauto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clientrequest.modelauto')),
            ],
        ),
    ]
