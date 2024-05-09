from django import forms
from .models import URLRecord

class URLForm(forms.ModelForm):
    class Meta:
        model = URLRecord
        fields = ['url']