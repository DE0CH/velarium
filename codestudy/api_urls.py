from django.urls import path
from . import api_views

app_name = 'codestudy-api'
urlpatterns = [
    path('', api_views.index, name='index'),
    path('tags/', api_views.tags, name='tags')
]