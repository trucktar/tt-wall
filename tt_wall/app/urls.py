from django.urls import path

from tt_wall.app import views

urlpatterns = [
    path('', views.index, name='home'),
]
