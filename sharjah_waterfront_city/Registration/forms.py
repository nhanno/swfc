from django import forms
from Registration.models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta():
        model=Registration
        fields=('First_Name','Last_Name','Email_Address','Mobile_Number','Intereset')

        widgets={
        'First_Name':forms.TextInput(attrs={'placeholder':'First Name'}),
        'Last_Name':forms.TextInput(attrs={'placeholder':'Last Name'}),
        'Email_Address':forms.TextInput(attrs={'placeholder':'Email Address'}),
        'Mobile_Number':forms.TextInput(attrs={'placeholder':'Contact Number (Example +9715XXXXXXXX)'}),
        # 'Intereset':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        'Intereset':forms.TextInput(attrs={'placeholder':'Please Share your Intereset Here ..'}),
        }
