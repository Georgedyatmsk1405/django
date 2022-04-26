from django import forms
from app_trans.models import News
from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.models import User

class NewsForm(forms.ModelForm):
    name = forms.CharField(max_length=32)
    description = forms.CharField(max_length=100,required=False)

    class Meta:
        model = News
        fields=('name','description')



class ExtendedRegisterForm(UserCreationForm):
    familyname=forms.CharField(max_length=30,required=False)
    description=forms.CharField(max_length=30,required=False)
    file = forms.FileField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'familyname', 'description','file')
