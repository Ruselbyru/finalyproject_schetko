# Generated by Django 3.2.4 on 2021-06-21 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandAuto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_auto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ModelAuto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_auto', models.CharField(max_length=50)),
                ('brandauto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientrequest.brandauto')),
            ],
        ),
    ]
