from django import forms

from django.contrib.auth  import models
from basic_app.models import UserProfileInfo


class UserProfileInfoForm(forms.ModelForm): 

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = models.User
        fields = ('username', 'password', 'email')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        # fields = ('username', 'email', 'password','portfolio', 'profile_pic')
        fields = ('profile_pic','portfolio')


