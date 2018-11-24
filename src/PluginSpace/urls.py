from django.urls import path

from . import views
urlpatterns = [
    path('index/', views.plugin_space_index, name='index'),
]