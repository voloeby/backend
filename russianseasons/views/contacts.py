from django.shortcuts import render
from russianseasons.decorators import *
from russianseasons.models import *
from russianseasons.forms.MessageForm import MessageForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.conf import settings


def shop_page(request):
	context = {}
	template_name = 'shop.html'
	context['items'] = ItemPrototype.objects.all()
	return render(request, template_name, context)


class ContactsView(View):
	template_name = 'contacts.html'

	def get(self, request):
		context = {}
		# context['site_key'] = settings.RECAPTCHA_SITE_KEY
		context['form'] = MessageForm()
		return render(request, self.template_name, context)

	def post(self, request):
		data = request.POST
		print(request.POST)
		form = MessageForm(request.POST)
		if form.is_valid():
			form.save()
			# msg.name = data['cName']
			# msg.email = data['cEmail']
			# msg.text = data['cMessage']
		# msg.save()
		else:
			print(form.errors)
		return HttpResponseRedirect(reverse('contacts_url'))
