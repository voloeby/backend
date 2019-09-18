from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class MainPagePost(models.Model):
    content = RichTextUploadingField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime']
