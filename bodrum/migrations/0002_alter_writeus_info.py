# Generated by Django 4.0.2 on 2022-04-17 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodrum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writeus',
            name='info',
            field=models.TextField(max_length=150, verbose_name=' İnfonu Giriniz:'),
        ),
    ]
