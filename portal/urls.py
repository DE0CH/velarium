from django.urls import path, include
from . import views


app_name = 'portal'
urlpatterns = [
    path('', views.index, name='index'),
    path('get-user/', views.install_keys, name='get-user'),
    path('demo-login/', views.demo_login, name='demo-login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('500/', views.invoke_500, name='invoke_500'),
]

