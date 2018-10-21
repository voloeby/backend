from django.shortcuts import render
from django.views import View
# Create your views here.

def home_page(request):
	template_name = 'home.html'
	return render(request, template_name)



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
		print(request)
