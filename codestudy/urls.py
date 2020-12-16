from django.urls import path
from . import views

app_name = 'codestudy'
urlpatterns = [
    path('results/', views.results, name='results'),
    path('', views.index, name='index'),
    path('add-paper/', views.add_paper, name='add-paper'),
    path('browse/<str:tag>', views.browse, name='browse')
]