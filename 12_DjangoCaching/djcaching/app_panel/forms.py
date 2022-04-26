from django import forms
from django.utils.translation import gettext_lazy as _

class HistoryForm(forms.Form):
    name = forms.CharField(max_length=32)
    description = forms.CharField(max_length=15)

