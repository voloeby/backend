import json
from django.shortcuts import render
from django.urls import reverse
# from django.views.generic import View
from django.views import View
from russianseasons.forms import *
from russianseasons.models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from russianseasons.admin.forms import *
from django.contrib.auth import authenticate, login, logout

sizes = ['s', 'm', 'l', 'xl']
colors = ['black', 'grey', 'white']

from django.utils.decorators import classonlymethod
from functools import update_wrapper

class BaseAdminView:

	"""
	Intentionally simple parent class for all views. Only implements
	dispatch-by-method and simple sanity checking.
	"""

	http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
	def __init__(self, **kwargs):
		"""
		Constructor. Called in the URLconf; can contain helpful extra
		keyword arguments, and other things.
		"""
		# Go through keyword arguments, and either save their values to our
		# instance, or raise an error.
		for key, value in kwargs.items():
			setattr(self, key, value)

	@classonlymethod
	def as_view(cls, **initkwargs):
		"""Main entry point for a request-response process."""
		for key in initkwargs:
			if key in cls.http_method_names:
				raise TypeError("You tried to pass in the %s method name as a "
								"keyword argument to %s(). Don't do that."
								% (key, cls.__name__))
			if not hasattr(cls, key):
				raise TypeError("%s() received an invalid keyword %r. as_view "
								"only accepts arguments that are already "
								"attributes of the class." % (cls.__name__, key))

		def view(request, *args, **kwargs):
			if not request.user.is_authenticated:
				raise Http404
			self = cls(**initkwargs)
			if hasattr(self, 'get') and not hasattr(self, 'head'):
				self.head = self.get
			self.request = request
			self.args = args
			self.kwargs = kwargs
			return self.dispatch(request, *args, **kwargs)
		view.view_class = cls
		view.view_initkwargs = initkwargs

		# take name and docstring from class
		update_wrapper(view, cls, updated=())

		# and possible attributes set by decorators
		# like csrf_exempt from dispatch
		update_wrapper(view, cls.dispatch, assigned=())
		return view

	def dispatch(self, request, *args, **kwargs):
		# Try to dispatch to the right method; if a method doesn't exist,
		# defer to the error handler. Also defer to the error handler if the
		# request method isn't on the approved list.
		if request.method.lower() in self.http_method_names:
			handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
		else:
			handler = self.http_method_not_allowed
		return handler(request, *args, **kwargs)

	def http_method_not_allowed(self, request, *args, **kwargs):
		logger.warning(
			'Method Not Allowed (%s): %s', request.method, request.path,
			extra={'status_code': 405, 'request': request}
		)
		return HttpResponseNotAllowed(self._allowed_methods())

	def options(self, request, *args, **kwargs):
		"""Handle responding to requests for the OPTIONS HTTP verb."""
		response = HttpResponse()
		response['Allow'] = ', '.join(self._allowed_methods())
		response['Content-Length'] = '0'
		return response

	def _allowed_methods(self):
		return [m.upper() for m in self.http_method_names if hasattr(self, m)]

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
		if request.user.is_authenticated:
			return HttpResponseRedirect(reverse('admin_shop_url'))
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

class SignInPage(View):
	template_name = 'admin/signin_page.html'
	context = {'signin_form': SignInForm()}
	def get(self, request):
		if request.user.is_authenticated:
			return HttpResponseRedirect(reverse('admin_shop_url'))
		return render(request, self.template_name, self.context)

	def post(self, request):
		context = {'signin_form': SignInForm()}
		form =SignInForm(request.POST)
		if form.is_valid():
			user = None
			try:
				user = User.objects.get(username=form.cleaned_data['username'])
			except User.DoesNotExist:
				user = None
			print(user)
			if user != None:
				context['error'] = True
				context['error_message'] = 'Неуникальный username.'
				context['signin_form'] = SignInForm(request.POST)
				return render(request, self.template_name, context)
			print(form.cleaned_data)
			user = User.objects.create_user(form.cleaned_data['username'], password=form.cleaned_data['password'], first_name=form.cleaned_data['first_name'])
			# user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user is None:
				context['error'] = True
				context['error_message'] = 'Не удалось создать пользователя.'
				return render(request, self.template_name, context)
			else:
				login(request, user)
				return HttpResponseRedirect(reverse('admin_shop_url'))
		else:
			context['error'] = True
			context['error_message'] = 'Неверно заполнена форма.' + str(form.errors)
			return render(request, self.template_name, context)

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
	template_name = 'admin/text_input_page.html'
	def get(self, request):
		context = {}
		context['form'] = TextInputForm()
		context['header'] = 'Добавить цвет'
		context['back_url'] = reverse('admin_shop_url')
		return render(request, self.template_name, context)
	def post(self, request):
		form = TextInputForm(request.POST)
		if form.is_valid():
			color = Color()
			color.name = form.cleaned_data['text']
			color.save()
		else:
			HttpResponseRedirect(reverse('new_color_url'))
		return HttpResponseRedirect(reverse('admin_shop_url'))

class NewSize(BaseAdminView):
	template_name = 'admin/text_input_page.html'
	def get(self, request):
		context = {}
		context['form'] = TextInputForm()
		context['header'] = 'Добавить размер'
		context['back_url'] = reverse('admin_shop_url')
		return render(request, self.template_name, context)
	def post(self, request):
		form = TextInputForm(request.POST)
		if form.is_valid():
			size = Size()
			size.name = form.cleaned_data['text']
			size.save()
		else:
			HttpResponseRedirect(reverse('new_size_url'))
		return HttpResponseRedirect(reverse('admin_shop_url'))

class BlogView(BaseAdminView):
	template_name = 'admin/blog_page.html'
	def get(self, request):
		context={}
		context['posts'] = BlogPost.objects.all()
		return render(request, self.template_name, context)

class NewBlogPostView(BaseAdminView):
	template_name = 'admin/blog_post_page.html'
	def get(self, request, id=None):
		context={}
		if id == None:
			obj = None
			context['header'] = 'Добавить пост'
		else:
			obj = get_object_or_404(BlogPost, id=id)
			context['header'] = 'Изменить пост'
		context['form'] = BlogPostForm(instance=obj)
		return render(request, self.template_name, context)
	def post(self, request, id=None):
		if id == None:
			obj = None
		else:
			obj = get_object_or_404(BlogPost, id=id)
		form = BlogPostForm(request.POST, request.FILES, instance=obj)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('admin_blog_url'))
		else:
			context['header'] = 'Добавить пост'
			context['form'] = form
			return render(request, self.template_name, context)
	def delete(self, request, id):
		obj = get_object_or_404(BlogPost, id=id)
		obj.delete()
		return HttpResponse('ok')


class MessagesView(BaseAdminView):
	template_name = 'admin/messages_page.html'
	def get(self, request):
		context = {}
		context['messages'] = Message.objects.all()
		return render(request, self.template_name, context)

class SubscribersView(BaseAdminView):
	template_name = 'admin/subscribers_page.html'
	def get(self, request):
		context = {}
		context['subscribers'] = Subscriber.objects.all()
		return render(request, self.template_name, context)

class AnotherView(BaseAdminView):
	template_name = 'admin/another_page.html'
	def get(self, request):
		context = {}
		context['storage'] = Storage.objects.all()
		return render(request, self.template_name, context)

class NewAnotherView(BaseAdminView):
	template_name = 'admin/text_input_page.html'
	def get(self, request, id=None):
		context = {}
		context['back_url'] = reverse('admin_another_url')
		context['header'] = 'Новая запись'
		obj = None
		if id!=None:
			obj = get_object_or_404(Storage, id=id)
		context['form'] = AnotherInputForm(instance=obj)
		return render(request, self.template_name, context)
	def post(self, request, id=None):
		obj = None
		if id!=None:
			obj = get_object_or_404(Storage, id=id)
		form = AnotherInputForm(request.POST, instance=obj)
		if form.is_valid:
			form.save()
			return HttpResponseRedirect(reverse('admin_another_url'))


class MainPagePostView(BaseAdminView):
	template_name = 'admin/main_page_posts_page.html'
	def get(self, request):
		context={}
		context['posts'] = MainPagePost.objects.all()
		return render(request, self.template_name, context)

class NewMainPagePostView(BaseAdminView):
	template_name = 'admin/main_page_post_page.html'
	def get(self, request, id=None):
		context={}
		if id == None:
			obj = None
			context['header'] = 'Добавить пост'
		else:
			obj = get_object_or_404(MainPagePost, id=id)
			context['header'] = 'Изменить пост'
		context['form'] = MainPagePostForm(instance=obj)
		return render(request, self.template_name, context)
	def post(self, request, id=None):
		if id == None:
			obj = None
		else:
			obj = get_object_or_404(MainPagePost, id=id)
		form = MainPagePostForm(request.POST, request.FILES, instance=obj)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('admin_main_page_posts_url'))
		else:
			context['header'] = 'Добавить пост'
			context['form'] = form
			return render(request, self.template_name, context)
	def delete(self, request, id):
		obj = get_object_or_404(MainPagePost, id=id)
		obj.delete()
		return HttpResponse('ok')

class ArtPage(BaseAdminView):
	template_name = 'admin/art_page.html'
	def get(self, request, id=None):
		context = {}
		context['photos'] = Art.objects.all()
		return render(request, self.template_name, context)

class NewArtPage(BaseAdminView):
	template_name = 'admin/new_art_page.html'
	def get(self, request, id=None):
		context={}
		if id == None:
			obj = None
			context['header'] = 'Добавить изображение'
		else:
			obj = get_object_or_404(Art, id=id)
			context['header'] = 'Изменить изображение'
		context['form'] = ArtForm(instance=obj)
		return render(request, self.template_name, context)
	def post(self, request, id=None):
		if id == None:
			obj = None
		else:
			obj = get_object_or_404(Art, id=id)
		form = ArtForm(request.POST, request.FILES, instance=obj)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('admin_art_url'))
		else:
			context['header'] = 'Добавить изображение'
			context['form'] = form
			return render(request, self.template_name, context)
	def delete(self, request, id):
		obj = get_object_or_404(Art, id=id)
		obj.delete()
		return HttpResponse('ok')

class ItemImage(BaseAdminView):
	def post(self, request, id):
		item = get_object_or_404(ItemPrototype, id=id)
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			obj = form.save()
			item.images.add(obj)
			path = obj.file.url
			return HttpResponse(json.dumps({'image': path, 'id': obj.id}))
		else:
			raise Http404
	def delete(self, request, id):
		image_id = request.body.decode("utf-8").split('&')[0].split('=')[1]
		obj = get_object_or_404(Image, id=image_id)
		obj.delete()
		return HttpResponse('ok')

class FinancesPage(BaseAdminView):
	template_name = 'admin/finance_page.html'
	def post(self, request):
		form = FinanceForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.save()
			return HttpResponse('ok')
		else:
			return HttpResponse('bad form')
	def get(self, request):
		context = {}
		context['form'] = FinanceForm()
		context['finances'] = FinanceItem.objects.all()
		if FinanceItem.objects.count() > 0:
			context['total'] = FinanceItem.total()
		return render(request, self.template_name, context)

class AdminPage(BaseAdminView):
	template_name = 'admin/admin_page.html'
	def post(self, request):
		pass
	def get(self, request):
		context = {}
		context['users'] = User.objects.all()
		return render(request, self.template_name, context)

class UsersPage(BaseAdminView):
	def patch(self, request):
		print(request.POST)
		return HttpResponse('ok')
	def post(self, request):
		if request.POST['type'] == 'is_active':
			try:
				user = User.objects.get(id=request.POST['user_id'])
				# for user in User.objects.all():
				# 	print(user)
					# user.delete()
				# p = Profile()
				# p.save()
				# p.user = user
				# p.save()
				user.profile.is_active = not user.profile.is_active
				user.save()
			except User.DoesNotExist:
				raise Http404
		return HttpResponse('ok')
