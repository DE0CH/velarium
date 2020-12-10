from django.urls import path
from . import views

app_name = 'codestudy'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('result/', views.search_result, name='search_result'),
    path('', views.sui, name='sui'),
]