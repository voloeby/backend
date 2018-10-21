from django.shortcuts import render
from django.urls import reverse
# from django.views.generic import View
from django.views import View
from russianseasons.forms import *
from russianseasons.models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from russianseasons.admin.forms import *
from django.contrib.auth import authenticate, login, logout

sizes = ['s', 'm', 'l', 'xl']
colors = ['black', 'grey', 'white']

class BaseAdminView(View):
	admin = True
	context = {}
	# def as_view(self):
	# 	super(BaseAdminView, self).as_view()

def admin_page(request):
	template_name = 'admin/admin_page.html'
	return render(request, template_name)


class NewItem(BaseAdminView):
	template_name='admin/item_page.html'
	def get(self, request):
		context = {}
		context['form'] = ItemForm()
		context['header'] = 'Создать вещь'
		return render(request, self.template_name, context)
	def post(self, request):
		context = {}
		form = ItemForm(request.POST, request.FILES)
		if form.is_valid():
			obj = form.save()
			return HttpResponseRedirect(reverse('admin_shop_url'))
		else:
			context['error'] = True
			context['error_message'] = 'Неверно заполнена форма.' + str(form.errors)
			context['form'] = ItemForm(instance=obj)
			return render(request, self.template_name, context)


class EditItem(BaseAdminView):
	template_name='admin/item_page.html'
	def get(self, request, id):
		context = {}
		context['item'] = get_object_or_404(ItemPrototype, id=id)
		context['form'] = ItemForm(instance=context['item'])
		context['header'] = 'Изменить вещь'
		return render(request, self.template_name, context)
	def post(self, request, id):
		context = {}
		obj = get_object_or_404(ItemPrototype, id=id)
		form = ItemForm(request.POST, request.FILES, instance=obj)
		if form.is_valid():
			print(form['image'])
			form.save()
			return HttpResponseRedirect(reverse('admin_shop_url'))
		else:
			context['error'] = True
			context['error_message'] = 'Неверно заполнена форма.' + str(form.errors)
			context['form'] = ItemForm(instance=obj)
			return render(request, self.template_name, context)
	def delete(self, request, id):
		obj = get_object_or_404(ItemPrototype, id=id)
		obj.delete()
		return HttpResponse('ok')
	def patch(self, request, id):
		obj = get_object_or_404(ItemPrototype, id=id)
		obj.show = not obj.show
		obj.save()
		return HttpResponse('ok')

class DelItem(BaseAdminView):
	def get(self, request, id):
		obj = get_object_or_404(ItemPrototype, id=id)
		obj.delete()
		return HttpResponseRedirect(reverse('admin_shop_url'))

def logout_page(request):
	logout(request)
	return HttpResponseRedirect(reverse('home_url'))

class LoginPage(View):
	template_name = 'admin/login_page.html'
	context = {'login_form': LoginForm()}
	def get(self, request):
		return render(request, self.template_name, self.context)

	def post(self, request):
		context = {'login_form': LoginForm()}
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user is None:
				context['error'] = True
				context['error_message'] = 'Неверный логин и/или пароль.'
				return render(request, self.template_name, self.context)
			else:
				login(request, user)
				return HttpResponseRedirect(reverse('admin_shop_url'))
		else:
			context['error'] = True
			context['error_message'] = 'Неверно заполнена форма.' + str(form.errors)
			return render(request, self.template_name, self.context)

class ShopPage(BaseAdminView):
	template_name = 'admin/shop_page.html'
	def get(self, request):
		context = {}
		template_name = 'admin/shop_page.html'
		context['items'] = ItemPrototype.objects.all()
		return render(request, template_name, context)

class OrdersPage(BaseAdminView):
	template_name = 'admin/orders_page.html'
	def get(self, request):
		context = {}
		context['orders'] = Order.objects.all()
		return render(request, self.template_name, context)

class NewColor(BaseAdminView):
	template_name = 'admin/color_page.html'
	def get(self, request):
		context = {}
		return render(request, self.template_name, context)

class NewSize(BaseAdminView):
	template_name = 'admin/size_page.html'
	def get(self, request):
		context = {}
		return render(request, self.template_name, context)
