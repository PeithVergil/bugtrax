from django import forms

from .models import Bug


class BugForm(forms.ModelForm):

    class Meta:
        model = Bug
        fields = (
            'title', 'description', 'severity', 'state', 'owner'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
