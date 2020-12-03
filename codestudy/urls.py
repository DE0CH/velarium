from django.urls import path

from . import views

app_name = 'codestudy'
urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.search_result, name='search_result')
]