# accounts/forms.py

from django import forms
from .models import GFG

class SuperuserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = GFG
        fields = ('phone', 'email', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
        return user
