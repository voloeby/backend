from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=10000, default='')
    email = models.CharField(max_length=10000, default='')
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime']
