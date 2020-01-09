import json
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from russianseasons.forms.forms import *
from russianseasons.models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from russianseasons.admin.forms import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


sizes = ['s', 'm', 'l', 'xl']
colors = ['black', 'grey', 'white']


class BaseAdminView(View):
	pass


def admin_page(request):
	template_name = 'admin/admin_page.html'
	return render(request, template_name)


class NewItem(BaseAdminView):
	template_name = 'admin/item_page.html'

	def get(self, request):
		context = {}
		context['form'] = NewItemForm()
		context['header'] = 'Создать вещь'
		return render(request, self.template_name, context)

	def post(self, request):
		context = {}
		form = NewItemForm(request.POST, request.FILES)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.number = ItemPrototype.objects.count() + 1
			obj.save()
			return HttpResponseRedirect(reverse('admin_shop_url'))
		else:
			context['error'] = True
			context['error_message'] = 'Неверно заполнена форма.' + str(form.errors)
			context['form'] = form
			return render(request, self.template_name, context)


class EditItem(BaseAdminView):
	template_name = 'admin/item_page.html'

	def get(self, request, id):
		context = {}
		context['item'] = get_object_or_404(ItemPrototype, id=id)
		context['form'] = EditItemForm(instance=context['item'])
		context['header'] = 'Изменить вещь'
		return render(request, self.template_name, context)

	def post(self, request, id):
		context = {}
		obj = get_object_or_404(ItemPrototype, id=id)
		form = EditItemForm(request.POST, request.FILES, instance=obj)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('admin_shop_url'))
		else:
			context['error'] = True
			context['error_message'] = 'Неверно заполнена форма.' + str(form.errors)
			context['form'] = EditItemForm(instance=obj)
			return render(request, self.template_name, context)

	def delete(self, request, id):
		obj = get_object_or_404(ItemPrototype, id=id)
		obj.delete()
		return HttpResponse('ok', content_type="application/json")

	def patch(self, request, id):
		obj = get_object_or_404(ItemPrototype, id=id)
		print(request.GET.get('type', None))
		if request.GET.get('type', None) == 'show':
			obj.show = not obj.show
			obj.save()
		elif request.GET.get('type', None) == 'move_up':
			number = obj.number
			if number == 1:
				return HttpResponse('no_change', content_type="application/json")
			try:
				prev = ItemPrototype.objects.get(number=number - 1)
				prev.number = number
				prev.save()
				obj.number = number - 1
				obj.save()
				return HttpResponse('ok', content_type="application/json")
			except ItemPrototype.DoesNotExist:
				obj.number = number - 1
				obj.save()
				return HttpResponse('no_change', content_type="application/json")
		elif request.GET.get('type', None) == 'move_down':
			number = obj.number
			if number == ItemPrototype.objects.count():
				return HttpResponse('no_change', content_type="application/json")
			try:
				next = ItemPrototype.objects.get(number=number + 1)
				next.number = number
				next.save()
				obj.number = number + 1
				obj.save()
				return HttpResponse('ok', content_type="application/json")
			except ItemPrototype.DoesNotExist:
				obj.number = number + 1
				obj.save()
				print(obj.number)
				return HttpResponse('no_change', content_type="application/json")
		return HttpResponse('ok', content_type="application/json")


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
			user = authenticate(
				request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
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
		form = SignInForm(request.POST)
		if form.is_valid():
			user = None
			try:
				user = User.objects.get(username=form.cleaned_data['username'])
			except User.DoesNotExist:
				user = None
			print(user)
			if user is not None:
				context['error'] = True
				context['error_message'] = 'Неуникальный username.'
				context['signin_form'] = SignInForm(request.POST)
				return render(request, self.template_name, context)
			print(form.cleaned_data)
			user = User.objects.create_user(
				form.cleaned_data['username'], password=form.cleaned_data['password'], first_name=form.cleaned_data['first_name'])
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
		context = {}
		context['posts'] = BlogPost.objects.all()
		return render(request, self.template_name, context)


class NewBlogPostView(BaseAdminView):
	template_name = 'admin/blog_post_page.html'

	def get(self, request, id=None):
		context = {}
		if id is None:
			obj = None
			context['header'] = 'Добавить пост'
		else:
			obj = get_object_or_404(BlogPost, id=id)
			context['header'] = 'Изменить пост'
		context['form'] = BlogPostForm(instance=obj)
		return render(request, self.template_name, context)

	def post(self, request, id=None):
		if id is None:
			obj = None
		else:
			obj = get_object_or_404(BlogPost, id=id)
		form = BlogPostForm(request.POST, request.FILES, instance=obj)
		if form.is_valid():
			model = form.save(commit=False)
			if not obj:
				model.user = request.user
			model.save()
			return HttpResponseRedirect(reverse('admin_blog_url'))
		else:
			context['header'] = 'Добавить пост'
			context['form'] = form
			return render(request, self.template_name, context)

	def delete(self, request, id):
		obj = get_object_or_404(BlogPost, id=id)
		obj.delete()
		return HttpResponse('ok', content_type="application/json")


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
		if id is not None:
			obj = get_object_or_404(Storage, id=id)
		context['form'] = AnotherInputForm(instance=obj)
		return render(request, self.template_name, context)

	def post(self, request, id=None):
		obj = None
		if id is not None:
			obj = get_object_or_404(Storage, id=id)
		form = AnotherInputForm(request.POST, instance=obj)
		if form.is_valid:
			form.save()
			return HttpResponseRedirect(reverse('admin_another_url'))


class MainPagePostView(BaseAdminView):
	template_name = 'admin/main_page_posts_page.html'

	def get(self, request):
		context = {}
		context['posts'] = MainPagePost.objects.all()
		return render(request, self.template_name, context)


class NewMainPagePostView(BaseAdminView):
	template_name = 'admin/main_page_post_page.html'

	def get(self, request, id=None):
		context = {}
		if id is None:
			obj = None
			context['header'] = 'Добавить пост'
		else:
			obj = get_object_or_404(MainPagePost, id=id)
			context['header'] = 'Изменить пост'
		context['form'] = MainPagePostForm(instance=obj)
		return render(request, self.template_name, context)

	def post(self, request, id=None):
		if id is None:
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
		return HttpResponse('ok', content_type="application/json")


class ArtPage(BaseAdminView):
	template_name = 'admin/art_page.html'

	def get(self, request, id=None):
		context = {}
		context['photos'] = Art.objects.all()
		return render(request, self.template_name, context)


class NewArtPage(BaseAdminView):
	template_name = 'admin/new_art_page.html'

	def get(self, request, id=None):
		context = {}
		if id is None:
			obj = None
			context['header'] = 'Добавить изображение'
		else:
			obj = get_object_or_404(Art, id=id)
			context['header'] = 'Изменить изображение'
		context['form'] = ArtForm(instance=obj)
		return render(request, self.template_name, context)

	def post(self, request, id=None):
		if id is None:
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
		return HttpResponse('ok', content_type="application/json")


class ItemImage(BaseAdminView):
	def post(self, request, id):
		item = get_object_or_404(ItemPrototype, id=id)
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			obj = form.save()
			item.images.add(obj)
			path = obj.file.url
			return HttpResponse(json.dumps({'image': path, 'id': obj.id}), content_type="application/json")
		else:
			raise Http404

	def delete(self, request, id):
		image_id = request.body.decode("utf-8").split('&')[0].split('=')[1]
		obj = get_object_or_404(Image, id=image_id)
		obj.delete()
		return HttpResponse('ok', content_type="application/json")


class FinancesPage(BaseAdminView):
	template_name = 'admin/finance_page.html'

	def post(self, request):
		form = FinanceForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.save()
			return HttpResponse('ok', content_type="application/json")
		else:
			return HttpResponse('bad form', content_type="application/json")

	def get(self, request):
		context = {}
		context['form'] = FinanceForm()
		context['finances'] = FinanceItem.objects.all()
		if FinanceItem.objects.count() > 0:
			context['total'] = FinanceItem.total()
		return render(request, self.template_name, context)

	def delete(self, request):
		try:
			try:
				FinanceItem.objects.get(id=request.body.decode(
					"utf-8").split('&')[0].split('=')[1]).delete()
			except FinanceItem.DoesNotExist:
				return HttpResponse('not_deleted', content_type="application/json")
		except Exception as e:
			return HttpResponse(e, content_type="application/json")
		return HttpResponse('ok', content_type="application/json")


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
		return HttpResponse('ok', content_type="application/json")

	def post(self, request):
		if request.POST['type'] == 'is_active':
			try:
				user = User.objects.get(id=request.POST['user_id'])
				user.profile.is_active = not user.profile.is_active
				user.save()
			except User.DoesNotExist:
				raise Http404
		return HttpResponse('ok', content_type="application/json")


class NewCategoryPage(BaseAdminView):
	template_name = 'admin/category_page.html'

	def get(self, request, id=None):
		context = {}
		category = None
		context['header'] = 'Добавить категорию'
		if id:
			try:
				category = Category.objects.get(id=id)
				context['header'] = 'Изменить категорию'
			except Category.DoesNotExist:
				raise Http404

		context['form'] = CategoryForm(instance=category)
		return render(request, self.template_name, context)

	def post(self, request, id=None):
		context = {}
		category = None
		if id:
			try:
				category = Category.objects.get(id=id)
				context['header'] = 'Изменить категорию'
			except Category.DoesNotExist:
				raise Http404
		form = CategoryForm(request.POST, instance=category)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('admin_categories_url'))
		else:
			context['error'] = True
			context['error_message'] = 'Неверно заполнена форма.' + str(form.errors)
			return render(request, self.template_name, context)


class CategoriesPage(BaseAdminView):
	template_name = 'admin/categories_page.html'

	def get(self, request):
		context = {}
		context['categories'] = Category.objects.all()
		return render(request, self.template_name, context)
