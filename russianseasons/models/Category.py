from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(default='')
    price = models.IntegerField(null=True, blank=True, default=1000)
    sale_price = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        if(self.sale_price):
            return self.name + ' ' + str(self.price) + '(' + str(self.sale_price) + ')'
        else:
            return self.name + ' ' + str(self.price)
