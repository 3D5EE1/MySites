from django.forms import ModelForm
from .models import ComingSoon


class ComingSoonForm(ModelForm):

    class Meta:
        model = ComingSoon
        fields = ['name', 'email', 'subject', 'message']