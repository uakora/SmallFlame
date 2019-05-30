from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.layui_space_index),
    path('demo/<int:demo_idx>', views.layui_demo_idx),
]