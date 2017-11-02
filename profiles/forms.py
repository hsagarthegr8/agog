from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user','image','lives_in','hometown','relationship','interests','about']
        widgets = {
            'relationship':forms.RadioSelect()
        }
