# Generated by Django 4.0.2 on 2022-04-17 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodrum', '0004_specialarea_writeus_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialarea',
            name='author',
            field=models.CharField(default=21, max_length=25, verbose_name='İsim Giriniz'),
            preserve_default=False,
        ),
    ]