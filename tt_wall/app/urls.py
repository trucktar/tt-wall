from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from tt_wall.app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search', views.category_search, name='search'),
    path('location/<location_name>', views.location_filter, name='filter'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
