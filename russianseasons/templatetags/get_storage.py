from russianseasons.models import Storage
from django import template

register = template.Library()


@register.simple_tag
def get_storage(*args):
    objects = Storage.objects.all()
    res = {}
    for item in objects:
        res[item.key] = item.value
    return res
