from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.layui_space_index, name='layui'),

]