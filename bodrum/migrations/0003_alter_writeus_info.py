# Generated by Django 4.0.2 on 2022-04-17 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodrum', '0002_alter_writeus_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writeus',
            name='info',
            field=models.TextField(max_length=300, verbose_name=' İnfonu Giriniz:'),
        ),
    ]
