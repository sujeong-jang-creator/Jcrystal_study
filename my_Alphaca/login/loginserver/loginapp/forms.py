from django import forms
from .models import Write

class WriteForm(forms.ModelForm):
    class Meta:
        model = Write
        fields = '__all__'