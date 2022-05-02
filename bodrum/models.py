from django.db import models
from django.urls import reverse
# Create your models here.


class Slider(models.Model):
    name = models.CharField(max_length=15, verbose_name='Slider Author')
    title = models.CharField(max_length=300, verbose_name='Yorum')
    small = models.CharField(max_length=300, verbose_name='Küçük Yazı')
    title2 = models.CharField(max_length=300, verbose_name='Yorum')
    small2 = models.CharField(max_length=300, verbose_name='Küçük Yazı')
    title3 = models.CharField(max_length=300, verbose_name='Yorum')
    small3 = models.CharField(max_length=300, verbose_name='Küçük Yazı')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)


    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=15, verbose_name='İsim Giriniz')
    info = models.TextField(max_length=300, verbose_name='Yorum')
    position = models.CharField(max_length=15,verbose_name='Pozizyon')


    def __str__(self):
        return self.name

class Cheff(models.Model):
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    name = models.CharField(max_length=15, verbose_name='İsim Giriniz')
    restaurant = models.CharField(max_length=15, verbose_name='Restanurant giriniz')

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


class About(models.Model):
    about = models.TextField(max_length=1000, verbose_name='Hakkımızda')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)


    def __str__(self):
        return self.about

class History(models.Model):
    about = models.TextField(max_length=1000, verbose_name='Hakkımızda')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)


    def __str__(self):
        return self.about

class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=20, db_index=True, unique=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bodrum:category_list', args=[self.slug])


class SubCategory(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    AltCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=20, db_index=True, unique=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bodrum:category_list', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)



    class Meta:
        ordering = ['-id']
        index_together = (('id', 'slug',))

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('bodrum:product_detail',args=[self.slug, self.id])

class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title