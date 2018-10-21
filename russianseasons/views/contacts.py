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


class ContactsView(View):
	template_name = 'contacts.html'
	def get(self, request):
		context = {}
		return render(request, self.template_name, context)
	def post(self, request):
		data = request.POST
		msg = Message()
		msg.name = data['cName']
		msg.email = data['cEmail']
		msg.text = data['cMessage']
		msg.save()
		return HttpResponseRedirect(reverse('contacts_url'))
