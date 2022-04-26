from django import forms
from app_files.models import File, News, Profil
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MultiFileForm(forms.Form):
    username = forms.CharField()
    familyname = forms.CharField(widget=forms.PasswordInput)
    description=forms.CharField(widget=forms.PasswordInput)
    file_filed = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class ExtendedRegisterForm(UserCreationForm):
    familyname=forms.CharField(max_length=30,required=False)
    description=forms.CharField(max_length=30,required=False)
    file = forms.FileField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'familyname', 'description','file')
class ExtendedRegisterrForm(forms.ModelForm):
    familyname = forms.CharField(max_length=30, required=False)
    description = forms.CharField(max_length=30, required=False)
    file = forms.FileField()
    class Meta:
        model=User
        fields = ('username','familyname', 'description', 'file')




class NewsForm(forms.ModelForm):
    name = forms.CharField(max_length=32)
    description = forms.CharField(max_length=100,required=False)
    attachments = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model=News
        fields=('name','description','attachments')
class SpecialForm(forms.Form):
    file = forms.FileField()
