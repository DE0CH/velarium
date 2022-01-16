from django.urls import path, include
from . import views


app_name = 'portal'
urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    path('add-paper/', views.add_paper, name='add-paper'),
    path('get-user/', views.install_keys, name='get-user'),
    path('add-paper/presign-s3', views.presign_s3, name='presign-s3'),
    path('edit-tags/', views.edit_tags, name='edit-tags'),
    path('edit-paper/<uuid:pk>/', views.edit_paper, name='edit-paper'),
    path('browse/<str:tag_class>/<str:tag>', views.browse, name='browse'),
    path('all-papers/', views.all_papers, name='all-papers'),
    path('login/', views.login, name='login'),
    path('admin/', views.admin, name='admin'),
    path('logout/', views.logout, name='logout'),
    path('bookmark/', views.bookmark, name='bookmark'),
    path('bookmarked/', views.bookmarked, name='bookmarked'),
    path('500/', views.invoke_500, name='invoke_500'),
]

