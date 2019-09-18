from django.db import models


class Image(models.Model):
    file = models.ImageField(upload_to='img/items/')
    name = models.CharField(max_length=1000, null=True, default=None)
    number = models.IntegerField(default=0)
