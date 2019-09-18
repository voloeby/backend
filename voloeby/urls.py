from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('', include('alfa.urls')),
    # path('i18n/', include('django.conf.urls.i18n')),
    # path('djadmin/', admin.site.urls),
	# path('admin/', include('admin.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('russianseasons.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
