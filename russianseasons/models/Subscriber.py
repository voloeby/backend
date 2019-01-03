from django.db import models

class Subscriber(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=10000, default='')
