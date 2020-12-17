from django.urls import path
from . import views

app_name = 'codestudy'
urlpatterns = [
    path('results/', views.results, name='results'),
    path('', views.index, name='index'),
    path('add-paper/', views.add_paper, name='add-paper'),
    path('edit-tags/', views.edit_tags, name='edit-tags'),
    path('browse/<str:tag_class>/<str:tag>', views.browse, name='browse'),
    # path('login', views.login, name='login')
]