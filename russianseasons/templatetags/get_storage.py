from django import template

register = template.Library()
from russianseasons.models import Storage

@register.simple_tag
def get_storage(*args):
	objects = Storage.objects.all()
	res = {}
	for item in objects:
		res[item.key] = item.value
		print(item.key, item.value)
	print(res['meta_art_description'])
	return res
