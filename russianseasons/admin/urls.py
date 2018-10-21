from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from django.views.generic import RedirectView

# from russianseasons import views
from russianseasons.admin import views

urlpatterns = [
	path('', views.admin_page, name='admin_url'),
	path('login', views.LoginPage.as_view(), name='login_url'),
	path('logout', views.logout_page, name='logout_url'),
	path('shop', views.ShopPage.as_view(), name='admin_shop_url'),
	path('orders', views.OrdersPage.as_view(), name='admin_orders_url'),
	url('^shop/item/new$', views.NewItem.as_view(), name='new_item_url'),
	path('shop/colors/new', views.NewColor.as_view(), name='new_color_url'),
	path('shop/sizes/new', views.NewSize.as_view(), name='new_size_url'),
	path('shop/item/edit/<int:id>', views.EditItem.as_view(), name='edit_item_url'),
	path('shop/item/delete/<int:id>', views.DelItem.as_view(), name='delete_item_url'),
	path('blog', views.BlogView.as_view(), name='admin_blog_url'),
	path('blog/posts/new', views.NewBlogPostView.as_view(), name='new_blog_post_url'),
	path('blog/posts/edit/<int:id>', views.NewBlogPostView.as_view(), name='edit_blog_post_url'),
	path('messages', views.MessagesView.as_view(), name='admin_messages_url'),
	path('subscribers', views.SubscribersView.as_view(), name='admin_subscribers_url'),
]
