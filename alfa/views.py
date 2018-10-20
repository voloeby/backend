from django.shortcuts import render
from alfa.models import *
from alfa.forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect

def theme_page(request, id):
	context = {}
	template_name = 'theme/theme_page.html'
	try:
		context['theme'] = Theme.objects.get(id=id)
		#
		# for item in context['theme'].yes_arguments.all():
		# 	item.delete()
		#
		context['yes_arguments'] = context['theme'].yes_arguments.exclude(text__isnull=True)
		context['no_arguments'] = context['theme'].no_arguments.all()
	except Exception as e:
		context['error'] = True
		context['error_message'] = 'Error.<br>' + str(e)
	return render(request, template_name, context)

def home_page(request):
	context = {}
	template_name = 'home/home_page.html'
	try:
		context['all_themes'] = Theme.objects.all()
		return render(request, template_name, context)
	except Exception as e:
		context['error'] = True
		context['error_message'] = 'Error.<br>' + str(e)
		return render(request, template_name, context)

def edit_theme_page(request, id=None):
	context = {}
	template_name = 'form_page.html'
	try:
		theme = Theme.objects.get(id=id)
	except Exception as e:
		theme = None
	context['form'] = ThemeForm(instance=theme)
	try:
		if request.method == 'POST':
			form = ThemeForm(request.POST, request.FILES, instance=theme)
			if form.is_valid():
				theme = form.save()
				return HttpResponseRedirect(reverse('theme_url', kwargs={'id': theme.id}))
			else:
				raise Exception('Form error. ' + str(form.errors))
		return render(request, template_name, context)
	except Exception as e:
		context['error'] = True
		context['error_message'] = 'Error.<br>' + str(e)
		return render(request, template_name, context)

def new_yes_argument_page(request, id):
	context = {}
	print(YesArgument.objects.all().count())
	try:
		theme = Theme.objects.get(id=id)

		if request.method == 'POST':
			form = YesArgumentForm(request.POST)
			if form.is_valid():
				argument = form.save(commit=False)
				print(argument.text)
				if argument.text != '':
					argument.theme = theme
					argument.save()
				theme.yes_count += 1
				theme.save()
				return HttpResponseRedirect(reverse('theme_url', kwargs={'id': id}))
			else:
				print(str(form.errors))
				raise Exception('Form error.' + str(form.errors))
		else:
			return HttpResponseRedirect(reverse('theme_url', kwargs={'id': id}))
	except Exception as e:
		context['error'] = True
		template_name = 'home/home_page.html'
		context['error_message'] = 'Error.<br>' + str(e)
		return render(request, template_name, context)

	return HttpResponseRedirect(reverse('home_url'))
