from django.urls import path

from . import views
urlpatterns = [
    path('index/', views.plugin_space_index, name='index'),
    path('datatable/learn01/', views.datatable_learn01, name='datatable'),
    path('datatable/learn02/', views.datatable_learn02, name='datatable'),
    path('datatable/learn03/', views.datatable_learn03, name='datatable'),
]