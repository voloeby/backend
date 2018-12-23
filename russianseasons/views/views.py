from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from russianseasons.models import *


def home_page(request):
    context = {}
    template_name = 'home.html'
    context['posts'] = MainPagePost.objects.all()
    return render(request, template_name, context)


def art_page(request):
    context = {}
    template_name = 'art.html'
    context['photos'] = Art.objects.all()
    return render(request, template_name, context)


def contacts_page(request):
    template_name = 'contacts.html'
    return render(request, template_name)


def blog_page(request):
    template_name = 'blog.html'
    return render(request, template_name)


def about_page(request):
    template_name = 'about.html'
    return render(request, template_name)


def cart_page(request):
    template_name = 'cart.html'
    return render(request, template_name)


class BaseView(View):
    context = {}


class SubscribeToEmail(View):
    def post(self, request):
        sub = Subscriber()
        sub.email = request.POST['email']
        sub.save()
        return HttpResponse('ok')
