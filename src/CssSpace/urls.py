from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.css_space_index, name='css'),
    path('demo_01/', views.css_demo_01, name='css'),
    path('demo_02/', views.css_demo_02, name='css'),
    path('demo_03/', views.css_demo_03, name='css'),
]