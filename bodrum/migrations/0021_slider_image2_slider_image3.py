# Generated by Django 4.0.2 on 2022-04-29 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodrum', '0020_alter_slider_small_alter_slider_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='image2',
            field=models.ImageField(blank=True, upload_to='products/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='slider',
            name='image3',
            field=models.ImageField(blank=True, upload_to='products/%y/%m/%d'),
        ),
    ]
