from django.conf.urls import url, include
from django.contrib import admin
from App import urls as urlsApp

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tulio/', include(urlsApp)),
]
