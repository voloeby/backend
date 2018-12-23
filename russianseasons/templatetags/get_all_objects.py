from django.apps import apps
from django import template

register = template.Library()


@register.simple_tag
def get_all_objects(obj_name, *args):
    obj = apps.get_model(app_label='alfa', model_name=obj_name)
    return obj.objects.all()
