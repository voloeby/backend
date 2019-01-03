from django.db import models
from .Item import Item
from django.contrib.auth.models import User


class Order(models.Model):
    city = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    is_preorder = models.BooleanField(default=True)
    items = models.ManyToManyField(Item)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime']
