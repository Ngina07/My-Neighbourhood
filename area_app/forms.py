from django import forms
from .models import Profile,Hood, notifications,Business

class notificationsForm(forms.ModelForm):
    class Meta:
        model=notifications
        exclude=['author','neighbourhood','post_date']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']


class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['owner','neighbourhood']
