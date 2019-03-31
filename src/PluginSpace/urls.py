from django.urls import path

from . import views
urlpatterns = [
    path('index/', views.plugin_space_index, name='index'),
    path('datatable/learn01/', views.datatable_learn01, name='datatable'),
    path('datatable/learn02/', views.datatable_learn02, name='datatable'),
    path('datatable/learn03/', views.datatable_learn03, name='datatable'),
    path('datatable/learn04/', views.datatable_learn04, name='datatable'),
    path('datatable/learn05/', views.datatable_learn05, name='datatable'),
    path('datatable/learn05/data', views.datatable_learn05_data, name='datatable'),

    path('datatable/demo/06', views.datatable_demo_06, name='datatable'),
    path('datatable/demo/06/log/data/', views.dt_demo_06_logs),

    path('datatable/data/year', views.datatable_data_year, name='datatable'),

    path('multiselect/learn01/', views.multiselect_learn01, name='multiselect'),
]