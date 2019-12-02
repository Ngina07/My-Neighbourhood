from django import forms
from .models import Profile,Hood, notifications,Business

class notificationsForm(forms.ModelForm):
    class Meta:
        model=notifications
        exclude=['author','neighbourhood','post_date']

