from django.conf.urls import url
from . import views


app_name = "Reception"
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^add/$', views.add, name='add'),
    url(r'^refer/(?P<n_id>[0-9]+)/$', views.refer, name='refer'),
    #url(r'^savenew/$', views.savenew, name='refer')

]