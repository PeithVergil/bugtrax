from django.conf.urls import url

from .views import BugListView, BugCreateView, BugDetailView


urlpatterns = [
    url(r'^list/$',
        BugListView.as_view(),
        name='list'),

    url(r'^create/$',
        BugCreateView.as_view(),
        name='create'),

    url(r'^(?P<pk>\d+)/detail/$',
        BugDetailView.as_view(),
        name='detail'),
]
