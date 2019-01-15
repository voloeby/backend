from django.urls import path
from django.conf.urls import include
from russianseasons.views import shop, blog, contacts, views


urlpatterns = [
    path('admin/', include('russianseasons.admin.urls')),
	path('', views.art_page, name='art_url'),
    path('', views.art_page, name='home_url'),
    path('shop', shop.shop_page, name='shop_url'),
    path('shop/item/<int:id>', shop.ItemView.as_view(), name='item_url'),
    path('contacts', contacts.ContactsView.as_view(), name='contacts_url'),
    path('blog', blog.blog_page, name='blog_url'),
    path('blog/post/<int:id>', blog.blog_post_page, name='blog_post_url'),
    path('about', views.about_page, name='about_url'),
    path('cart', views.cart_page, name='cart_url'),
    path('subscribe_to_email', views.SubscribeToEmail.as_view(), name='subscribe_to_email_url'),
]
