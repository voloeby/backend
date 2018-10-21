from django.shortcuts import render
from django.shortcuts import get_object_or_404
from russianseasons.models import *

def blog_page(request):
	context = {}
	template_name = 'blog.html'
	context['posts'] = BlogPost.objects.all()
	return render(request, template_name, context)

def blog_post_page(request, id):
	context = {}
	context['post'] = get_object_or_404(BlogPost, id=id)
	template_name = 'blog_post.html'
	return render(request, template_name, context)
