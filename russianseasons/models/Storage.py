from django.db import models


class Storage(models.Model):
    key = models.CharField(max_length=100, default='')
    value = models.TextField(default=None, null=True, blank=True)

    def get(self, key):
        try:
            return Storage.objects.get(key=key)
        except Storage.DoesNotExist:
            return None

    def set(self, key, value):
        obj = None
        try:
            obj = Storage.objects.get(key=key)
        except Storage.DoesNotExist:
            pass
        obj = Storage(key=key, value=value)
        obj.save()
        return
