from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
	name = models.CharField(max_length=1000)

class Image(models.Model):
	file = models.ImageField()
	name = models.CharField(max_length=1000, null=True)

class Color(models.Model):
	name = models.CharField(max_length=1000)
	def __str__(self):
		return self.name

class Size(models.Model):
	name = models.CharField(max_length=1000)
	def __str__(self):
		return self.name



class ItemPrototype(models.Model):
	categories = models.ManyToManyField(Category)
	# images = models.ManyToManyField(Image)
	image = models.ImageField(upload_to='img/items/')
	sizes = models.ManyToManyField(Size)
	name = models.CharField(max_length = 1000)
	description = models.CharField(max_length=10000, null=True)
	colors = models.ManyToManyField(Color)
	price = models.IntegerField(null=True)
	show = models.BooleanField(default=False)

class Item(models.Model):
	color = models.ForeignKey(Color, on_delete=models.CASCADE)
	size = models.ForeignKey(Size, on_delete=models.CASCADE)
	sex = models.CharField(max_length=2)
	number = models.IntegerField(default=0)
	sold = models.IntegerField(default=0)
	prototype = models.ForeignKey(ItemPrototype, on_delete=models.CASCADE)

class Order(models.Model):
	city = models.CharField(max_length=1000)
	email = models.CharField(max_length=1000)
	is_preorder = models.BooleanField(default=True)
	items = models.ManyToManyField(Item)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
	datetime = models.DateTimeField(auto_now_add=True)

class MyUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	cart = models.ManyToManyField(Item)


class BlogPost(models.Model):
	title = models.CharField(max_length = 10000, default = '')
	content = RichTextUploadingField(blank=True, null=True)
	image = models.ImageField(upload_to='img/blog/')
	datetime = models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering = ['-datetime']

class Message(models.Model):
	name = models.CharField(max_length = 10000, default = '')
	email = models.CharField(max_length = 10000, default = '')
	text = models.TextField()
	datetime = models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering = ['-datetime']

class Subscriber(models.Model):
	datetime = models.DateTimeField(auto_now_add=True)
	email = models.CharField(max_length = 10000, default = '')

class Storage(models.Model):
	key = models.CharField(max_length=100, default='')
	value = models.TextField()
	def get(key):
		try:
			return Storage.objects.get(key=key)
		except:
			return None
