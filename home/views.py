from django.core.urlresolvers import reverse
from django.views.generic import RedirectView


class HomeRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('bugs:list')
