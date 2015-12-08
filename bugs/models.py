from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Bug(models.Model):

    title = models.CharField('title', max_length=200)

    description = models.TextField('description')

    STATE_OPEN = 1
    STATE_CLOSED = 2
    STATE_ASSIGNED = 3

    STATE_CHOICES = (
        (STATE_OPEN, 'Open'),
        (STATE_CLOSED, 'Closed'),
        (STATE_ASSIGNED, 'Assigned'),
    )

    state = models.SmallIntegerField('state',
                                     choices=STATE_CHOICES,
                                     default=STATE_OPEN)

    SEVERITY_LOW = 1
    SEVERITY_MEDIUM = 2
    SEVERITY_HIGH = 3
    SEVERITY_TRIVIAL = 4
    SEVERITY_CRITICAL = 5

    SEVERITY_CHOICES = (
        (SEVERITY_LOW, 'Low'),
        (SEVERITY_MEDIUM, 'Medium'),
        (SEVERITY_HIGH, 'High'),
        (SEVERITY_TRIVIAL, 'Trivial'),
        (SEVERITY_CRITICAL, 'Critical'),
    )

    severity = models.SmallIntegerField('severity',
                                        choices=SEVERITY_CHOICES,
                                        default=SEVERITY_MEDIUM)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='owner')

    # Date the bug was created.
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('bugs:detail', args=(self.id,))
