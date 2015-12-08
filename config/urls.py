from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

# Custom apps
urlpatterns += [
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^bugs/', include('bugs.urls', namespace='bugs')),
    url(r'^', include('home.urls', namespace='home')),
]
