from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('mainpage.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^reception/', include('Reception.urls')),
    url(r'^doctor/', include('Doctors.urls')),
]
