from django.db import models
from django.contrib.auth.models import User



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

class Item(models.Model):
	color = models.ForeignKey(Color, on_delete=models.CASCADE)
	size = models.ForeignKey(Size, on_delete=models.CASCADE)
	sex = models.CharField(max_length=2)
	number = models.IntegerField()
	sold = models.IntegerField()

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

class Order(models.Model):
	is_preorder = models.BooleanField()
	items = models.ManyToManyField(Item)
	user = models.ManyToManyField(User)

class MyUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	cart = models.ManyToManyField(Item)
