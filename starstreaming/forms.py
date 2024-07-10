from django import forms 
from . models import mysigninform,Registermovie

class signinform(forms.ModelForm):
    class Meta:
        model = mysigninform
        fields = ('Username','email','password')
        widgets = {
            'password': forms.PasswordInput(), 
        }

class movieRegisterForm(forms.ModelForm):
    class Meta:
        model = Registermovie
        fields = ('Name','Year','categories','Durection','descriptions','image','video')