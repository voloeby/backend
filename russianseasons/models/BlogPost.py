from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=10000, default='')
    content = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to='img/blog/')
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_DEFAULT)

    class Meta:
        ordering = ['-datetime']
