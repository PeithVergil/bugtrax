from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from .forms import BugForm
from .models import Bug


class BugViewMixin(LoginRequiredMixin):
    model = Bug


class BugListView(BugViewMixin, ListView):
    pass


class BugCreateView(BugViewMixin, CreateView):
    form_class = BugForm


class BugDetailView(BugViewMixin, DetailView):
    pass
