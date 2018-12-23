from django.shortcuts import render
from russianseasons.decorators import *
from russianseasons.models import *
from django.views import View
from django.http import HttpResponseRedirect


def shop_page(request):
    context = {}
    template_name = 'shop.html'
    context['items'] = ItemPrototype.objects.all()
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
