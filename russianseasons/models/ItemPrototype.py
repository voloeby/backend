from django.db import models
from .Category import Category
from .Image import Image
from .Size import Size
from .Color import Color


class ItemPrototype(models.Model):
    category = models.ForeignKey(Category, null=True, default=None,
                                 on_delete=models.SET_NULL, blank=True, related_name='items')
    images = models.ManyToManyField(Image, related_name='item')
    # main_image = models.OneToOneField(Image, on_delete=models.CASCADE, related_name='item')
    # image = models.ImageField(upload_to='img/items/')
    sizes = models.ManyToManyField(Size, blank=True, default=None)
    name = models.CharField(max_length=1000)
    sub_name = models.CharField(max_length=1000, default='')
    description = models.CharField(max_length=10000, null=True)
    colors = models.ManyToManyField(Color, blank=True, default=None)
    price = models.IntegerField(null=True)
    show = models.BooleanField(default=False)
    in_stock = models.BooleanField(default=True)
    is_new = models.BooleanField(default=True)
    number = models.IntegerField(default=0)

    class Meta:
        ordering = ['number']
