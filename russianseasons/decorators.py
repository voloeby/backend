from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404

def has_premission():
	def has(f):
		def func(request, *args, **kwargs):
			if request.user.is_superuser:
				return f(request, *args, **kwargs)
			else:
				raise Http404("Page not found")
		return func
	return has
