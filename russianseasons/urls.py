from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from django.views.generic import RedirectView

# from russianseasons import views
from russianseasons.views import shop, blog, views
from russianseasons.decorators import *

urlpatterns = [
	url('^admin/', include('russianseasons.admin.urls')),
	path('', views.home_page, name='home_url'),
	url('^shop$', shop.shop_page, name='shop_url'),
	url('^shop/item/(?P<id>\d+)$', shop.ItemView.as_view(), name='item_url'),
	url('^contacts$', views.contacts_page, name='contacts_url'),
	url('^blog$', blog.blog_page, name='blog_url'),
	url('^blog/post/(?P<id>\d+)$', blog.blog_post_page, name='blog_post_url'),
	url('^about$', views.about_page, name='about_url'),
	url('^cart$', views.cart_page, name='cart_url'),
	path('subscribe_to_email', views.SubscribeToEmail.as_view(), name='subscribe_to_email_url'),
]
