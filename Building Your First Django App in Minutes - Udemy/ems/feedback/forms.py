from django import forms
from .models import Feedback
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator
from myems.models import Employees

class FeedbackAddForm(forms.ModelForm):

    email = forms.CharField(widget = forms.TextInput(attrs={'size': 20}), validators=[EmailValidator(), MinLengthValidator(7), MaxLengthValidator(20)])
    comment = forms.CharField(widget = forms.Textarea(attrs={'rows': 6, 'cols': 60, 'style': 'resize:none;'}))
    
    def clean_emp_no(self):
        print(self.cleaned_data)
        emp_no = self.cleaned_data.get('emp_no')
   
        # if emp_no and not Employees.objects.filter(pk=emp_no).exists():
        #     raise forms.ValidationError("Invalid employee number")     

        return self.cleaned_data.get('emp_no')

    def clean(self):
        formData = super(FeedbackAddForm, self).clean()
        category = formData.get('category')
        comment = formData.get('comment')

        if category == '5':
            if 'emp_no=' not in comment:
                raise forms.ValidationError("Your complaint should have tab emp_no=")
            return formData
            
    class Meta:
        model = Feedback
        fields = ('emp_no', 'name', 'category', 'email', 'subject', 'is_read')

class FeedbackForm(forms.ModelForm):

    email = forms.CharField(widget = forms.TextInput(attrs={'size': 20}), validators=[EmailValidator()])
    comment = forms.CharField(widget = forms.Textarea(attrs={'rows': 6, 'cols': 60, 'style': 'resize:none;'}))
    created_on = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'size': 38}))

    class Meta:
        model = Feedback
        fields = '__all__'