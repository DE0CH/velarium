from django.urls import path, include
from codestudy import views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path('', include('codestudy.urls'))
]

handler404 = views.handler404
handler500 = views.handler500
handler403 = views.handler403
handler400 = views.handler400
