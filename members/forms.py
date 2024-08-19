from django import forms
from .models import Members
from .models import Video

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = {'name','Useremail','password'}


