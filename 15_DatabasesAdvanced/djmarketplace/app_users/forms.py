from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import SelectDateWidget

from django.contrib.auth.models import User

class ExtendedRegisterForm(UserCreationForm):
    familyname = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'familyname')