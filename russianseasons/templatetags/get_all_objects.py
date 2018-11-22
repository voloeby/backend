from django import template

register = template.Library()
from django.apps import apps

@register.simple_tag
def get_all_objects(obj_name, *args):
	obj = apps.get_model(app_label='alfa', model_name=obj_name)
	return obj.objects.all()
