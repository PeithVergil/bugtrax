from django.conf.urls import url

from .views import HomeRedirectView


urlpatterns = [
    url(r'^$',
        HomeRedirectView.as_view(),
        name='view'),
]
