from django import forms # type: ignore

class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    email = forms.EmailField(label='Email')
    date = forms.DateField(label='Date of Birth')
    occupation = forms.CharField(max_length=30, label='Occupation')