from django.urls import path
from admin.shop.views import ShopPage


urlpatterns = [
    path('', views.ShopView.as_view(), name='admin_shop_url'),
    # path('categories/new', views.NewCategoryPage.as_view(), name='admin_new_category_url'
    #      ),
    # path('categories/<int:id>/edit',
    #      views.NewCategoryPage.as_view(), name='admin_edit_category_url'),
    # path('categories', views.CategoriesPage.as_view(), name='admin_categories_url'),
    # path('item/new', views.NewItem.as_view(), name='new_item_url'),
    # path('colors/new', views.NewColor.as_view(), name='new_color_url'),
    # path('sizes/new', views.NewSize.as_view(), name='new_size_url'),
    # path('item/<int:id>/item_image', views.ItemImage.as_view(), name='admin_item_image_url'),
    # path('item/edit/<int:id>', views.EditItem.as_view(), name='edit_item_url'),
    # path('item/delete/<int:id>', views.DelItem.as_view(), name='delete_item_url'),
]
