from .models import Tracks, Avatars
from django.forms import ModelForm, TextInput
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TracksForm(ModelForm):
    source = forms.FileField()
    track_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Название трека: ', 'class': 'trackname'}))
    class Meta:
        model = Tracks
        fields = ['source', 'track_name']

class UserEditForm(ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email']

class AvatarsForm(ModelForm):
    class Meta:
        model = Avatars
        fields = ['image']
