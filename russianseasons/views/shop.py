from django.shortcuts import render
from django.shortcuts import get_object_or_404
from russianseasons.decorators import *
from russianseasons.models import *
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse

def shop_page(request):
	context = {}
	template_name = 'shop.html'
	# for i in ItemPrototype.objects.all():
	# 	i.delete()
	context['items'] = ItemPrototype.objects.all()
	# for item in context['items']:
	# 	item.image = item.images.all()[0]

	return render(request, template_name, context)


class ItemView(View):
	def get(self, request, id):
		context = {}
		template_name = 'item_page.html'
		item = get_object_or_404(ItemPrototype, id=id)
		context['item'] = item
		return render(request, template_name, context)
	def post(self, request, id):
		item_prot = get_object_or_404(ItemPrototype, id=id)
		color, created = Color.objects.get_or_create(name=request.POST['color'])
		size, created = Size.objects.get_or_create(name=request.POST['size'])
		item, created = Item.objects.get_or_create(color=color, size=size, prototype=item_prot)
		order = Order()
		order.save()
		order.is_preorder = True
		order.email = request.POST['email']
		order.city = request.POST['city']
		order.items.add(item)
		print(request.user)
		# order.user = request.user
		order.save()
		return HttpResponse('ok')
