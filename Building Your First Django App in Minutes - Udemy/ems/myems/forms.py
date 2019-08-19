
from django import forms
from .models import Employees
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator

class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(widget = forms.TextInput(attrs={'size': 20}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={'size': 20}))
    # comment = forms.CharField(widget = forms.Textarea(attrs={'rows': 6, 'cols': 60, 'style': 'resize:none;'}))
    created_on = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'size': 38}))

    class Meta:
        model = Employees
        fields = '__all__'