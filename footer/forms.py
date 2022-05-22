from .models import Support
from django import forms
from django.forms import ModelForm

class SupportForm(ModelForm):
    email = forms.EmailField(max_length=50, required=True)
    class Meta:
        model = Support
        fields = ['email', 'text']
