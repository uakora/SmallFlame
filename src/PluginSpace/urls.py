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

    path('datatable/demo/07', views.datatable_demo_07, name='datatable'),
    path('datatable/demo/08', views.datatable_demo_08, name='datatable'),
    path('datatable/demo/09', views.datatable_demo_09, name='datatable'),
    path('datatable/demo/10', views.datatable_demo_10, name='datatable'),


    path('datatable/data/year', views.datatable_data_year, name='datatable'),

    path('multiselect/learn01/', views.multiselect_learn01, name='multiselect'),

    path('draggable/demo/01', views.draggable_demo_01),
    path('draggable/demo/02', views.draggable_demo_02),
    path('draggable/demo/03', views.draggable_demo_03),
    path('draggable/demo/04', views.draggable_demo_04),
    path('draggable/demo/05', views.draggable_demo_05),
    path('draggable/demo/06', views.draggable_demo_06),
    path('draggable/demo/07', views.draggable_demo_07),
    path('draggable/demo/08', views.draggable_demo_08),
    path('draggable/demo/09', views.draggable_demo_09),
    path('draggable/demo/10', views.draggable_demo_10),
    path('draggable/demo/11', views.draggable_demo_11),

]