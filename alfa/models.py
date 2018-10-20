from django.db import models
from django.contrib.auth.models import User

class Theme(models.Model):
	name = models.CharField(max_length=1000, null=True, default=None)
	yes_count = models.IntegerField(default=0)
	no_count = models.IntegerField(default=0)


class Argument(models.Model):
	text = models.TextField(null=True, default=None, blank=True)
	user = models.ManyToManyField(User, related_name='arguments')
	is_anonymous = models.BooleanField(default=True, blank=True)
	datetime = models.DateTimeField(auto_now=True)
	number_of_likes = models.IntegerField(default=0)
	liked_by = models.ManyToManyField(User, related_name='likes')
	def __str__(self):
		return self.text
	class Meta:
		ordering = ['-number_of_likes', '-datetime']

class YesArgument(Argument):
	theme = models.ForeignKey(Theme, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='yes_arguments')

class NoArgument(Argument):
	theme = models.ForeignKey(Theme, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='no_arguments')

class Comment(models.Model):
	text = models.TextField(null=True, default=None, blank=True)
	argument = models.ForeignKey(Argument, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='comments')
