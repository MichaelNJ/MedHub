from django.conf.urls import url
from . import views

app_name = "Doctor"

urlpatterns = [
    url(r'^$', views.waiting, name='index'), 
    url(r'^waiting/$', views.index, name='waiting'),   
]