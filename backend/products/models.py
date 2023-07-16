from django.db import models
from django.template.defaultfilters import slugify

from versatileimagefield.fields import VersatileImageField, PPOIField


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(blank=True, null=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save()


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = VersatileImageField(upload_to='images/', ppoi_field='image_ppoi')
    image_ppoi = PPOIField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated_at']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save()
