from django.db import models


class Art(models.Model):
    link = models.URLField(max_length=300, blank=False, default=None, null=True)
    image = models.ImageField(upload_to='img/art/')
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime']
