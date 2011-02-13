from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label=u'Username', max_length=30)
    email = forms.EmailField(label=0'Email')
    password1 = forms.CharField(
        label = u'Password',
        widget = forms.PasswordInput()
    )
    password2 = forms.CharField(
        label = u'Password (again)',
        widget = forms.PasswordInput()
    )

def clean_password2(self):
    if 'password1' in self.cleaned_data:
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 == password2:
            return password2
    raise forms.ValidationError('Passwords do not match.')
