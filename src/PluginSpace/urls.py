from django.urls import path

from . import views
urlpatterns = [
    path('index/', views.plugin_space_index, name='index'),

    path('datatables/demo/<int:demo_idx>', views.datatables_demo_idx),
    path('echarts/demo/<int:demo_idx>', views.echarts_demo_idx),
    path('highcharts/demo/<int:demo_idx>', views.highcharts_demo_idx),
    path('datetimepicker/demo/<int:demo_idx>', views.datetimepicker_demo_idx),
    path('draggable/demo/<int:demo_idx>', views.draggable_demo_idx),
    path('droppable/demo/<int:demo_idx>', views.droppable_demo_idx),
    path('sortable/demo/<int:demo_idx>', views.sortable_demo_idx),

    path('datatable/learn02/', views.datatable_learn02, name='datatable'),
    path('datatable/learn03/', views.datatable_learn03, name='datatable'),
    path('datatable/learn04/', views.datatable_learn04, name='datatable'),
    path('datatable/learn05/', views.datatable_learn05, name='datatable'),
    path('datatable/learn05/data', views.datatable_learn05_data, name='datatable'),
    path('datatable/learn06', views.datatable_demo_06, name='datatable'),
    path('datatable/demo/06/log/data/', views.dt_demo_06_logs),
    path('datatable/learn07', views.datatable_demo_09, name='datatable'),
    path('datatable/learn08', views.datatable_demo_10, name='datatable'),


    path('datatable/data/year', views.datatable_data_year, name='datatable'),

    path('multiselect/learn01/', views.multiselect_learn01, name='multiselect'),

    path('datatables/data/mr/config/list', views.mr_config_list)
]