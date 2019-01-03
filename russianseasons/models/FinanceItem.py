from django.db import models
from django.contrib.auth.models import User

class FinanceItem(models.Model):
    user = models.ForeignKey(User, related_name='finances', on_delete=models.SET_NULL, null=True)
    text = models.TextField(blank=False, default='', null=False)
    money = models.IntegerField()
    is_income = models.BooleanField(null=False, default=True)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime']

    def total():
        result = 0
        for item in FinanceItem.objects.all():
            if item.is_income:
                result += int(item.money)
            else:
                result -= int(item.money)
        return result
