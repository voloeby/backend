from django.shortcuts import render
from django.shortcuts import get_object_or_404
from russianseasons.decorators import *
from russianseasons.models import *

def shop_page(request):
	context = {}
	template_name = 'shop.html'
	# for i in ItemPrototype.objects.all():
	# 	i.delete()
	context['items'] = ItemPrototype.objects.all()
	# for item in context['items']:
	# 	item.image = item.images.all()[0]

	return render(request, template_name, context)

def item_page(request, id):
	context = {}
	template_name = 'item_page.html'
	item = get_object_or_404(ItemPrototype, id=id)
	# item.image = item.images.all()[0]
	context['item'] = item
	# print(item.image.file.url)
	return render(request, template_name, context)
