from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class BlogPost(models.Model):
    title = models.CharField(max_length=10000, default='')
    content = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to='img/blog/')
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime']
