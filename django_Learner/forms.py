from django import forms
from .models import Info

class StudentForm(forms.ModelForm):
    class Meta:
        model=Info
        fields=['name','age','email','College_Name']