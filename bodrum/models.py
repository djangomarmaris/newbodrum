from django.db import models
from PIL import Image
# Create your models here.



class WriteUS(models.Model):
    author = models.CharField(max_length=25,verbose_name='İsim Giriniz')
    info = models.TextField(max_length=300,verbose_name=" İnfonu Giriniz:")

    def __str__(self):
        return self.author


class SpecialArea(models.Model):
    author = models.CharField(max_length=25, verbose_name='İsim Giriniz')
    info = models.TextField(max_length=300, verbose_name=" İnfonu Giriniz:")
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image_info = models.CharField(max_length=15, verbose_name='Mini Resim İnfosu 15 Karakterlik')
    image2 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image_info2 = models.CharField(max_length=15, verbose_name='Mini Resim İnfosu 15 Karakterlik')
    image3 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image_info3 = models.CharField(max_length=15, verbose_name='Mini Resim İnfosu 15 Karakterlik')
    image4 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image_info4 = models.CharField(max_length=15, verbose_name='Mini Resim İnfosu 15 Karakterlik')
    image5 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image_info5 = models.CharField(max_length=15, verbose_name='Mini Resim İnfosu 15 Karakterlik')

    def __str__(self):
        return self.author



class Comment(models.Model):
    name = models.CharField(max_length=15, verbose_name='İsim Giriniz')
    info = models.TextField(max_length=300, verbose_name='Yorum')
    position = models.CharField(max_length=15,verbose_name='Pozizyon')


    def __str__(self):
        return self.name



class Subscribe(models.Model):
    email = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return self.email


class Parthners(models.Model):
    name = models.CharField(max_length=15, verbose_name='Firma İsmi giriniz')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    katalog = models.FileField(upload_to='products/katalog/%y/%m/%d')


    def __str__(self):
        return self.name


class Galeri(models.Model):
    info = models.CharField(max_length=250,default='Ürün Açıklama')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)


    def __str__(self):
        return self.info