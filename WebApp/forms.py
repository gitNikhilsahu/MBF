from django import forms
from WebApp.models import Emp

class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = '__all__'