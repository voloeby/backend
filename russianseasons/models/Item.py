from django.db import models
from .Color import Color
from .Size import Size
from .ItemPrototype import ItemPrototype


class Item(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    sex = models.CharField(max_length=2)
    number = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    prototype = models.ForeignKey(ItemPrototype, on_delete=models.CASCADE)
