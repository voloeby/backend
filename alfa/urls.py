from alfa import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.home_page, name = 'home_url'),
	url(r'^theme/(?P<id>\d+)$', views.theme_page, name = 'theme_url'),
	url(r'^theme/(?P<id>\d+)/argument/new$', views.new_yes_argument_page, name = 'new_yes_argument_url'),
	url(r'^theme/new$', views.edit_theme_page, name = 'new_theme_url'),
	url(r'^theme/edit/(?P<id>\d+)$', views.edit_theme_page, name = 'edit_theme_url'),
	]
