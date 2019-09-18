from django.db import models


class Size(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
