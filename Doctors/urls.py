from django.conf.urls import url
from . import views

app_name = "Doctor"

urlpatterns = [
    url(r'^$', views.waiting, name='waiting'),

    url(r'^record/(?P<r_id>[0-9]+)/$', views.record, name='record'),
]