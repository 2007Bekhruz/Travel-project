from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from accounts.models import CustomerUser

# Create your models here.


class Category(models.Model):
    title = models.CharField(verbose_name='Enter the category name ', max_length=150)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_service', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Services(models.Model):
    title = models.CharField(verbose_name='Enter the service name ', max_length=150)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Products(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(verbose_name='Describe your product')
    price = models.IntegerField(verbose_name='Price of your product')
    is_available = models.BooleanField(verbose_name='Is it available now', default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    services = models.ForeignKey(Services, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    def get_first_photo(self):
        photo = self.productimage_set.all().first()
        if photo is not None:
            return photo.photo.url
        return "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScL8Dl30mCY7X7M7y1JK7xTjONaYvIb2twnYNWCtwSC3VPONSNLJjcVtYF6LpL8ao8ar0&usqp=CAU"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug == slugify(self.title)
        return super().save(*args, **kwargs)


class ProductImage(models.Model):
    photo = models.ImageField(verbose_name='Product photo', upload_to='products/', blank=True, null=True)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
