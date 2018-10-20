from django.shortcuts import render
from django.shortcuts import get_object_or_404

def blog_page(request):
	template_name = 'blog.html'
	return render(request, template_name)

def blog_post_page(request, id):
	template_name = 'blog_post_page.html'
	return render(request, template_name)
