from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm (UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username', 'email', 'password1','password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','phone','image']

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Si hay un archivo, usa el nombre original
        if 'image' in self.cleaned_data and self.cleaned_data['image']:
            instance.image.name = self.cleaned_data['image'].name  # Conserva el nombre original
        if commit:
            instance.save()
        return instance