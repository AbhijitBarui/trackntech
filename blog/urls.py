from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('contents/', include('contents.urls')),
    path('accounts/', include('accounts.urls')),
    path('interests/', include('interests.urls')),
    path('votes/', include('votes.urls')),
    path('follows/', include('follows.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
