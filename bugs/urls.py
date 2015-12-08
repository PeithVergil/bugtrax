from django.conf.urls import url

from .views import BugListView, BugCreateView, BugDetailView, BugUpdateView


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

    url(r'^(?P<pk>\d+)/update/$',
        BugUpdateView.as_view(),
        name='update'),
]
