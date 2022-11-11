from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class LoginForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={"class":"form-control"}
        )
    )

    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class":"form-control"}
        )
    )

# class SignupForm(UserCreationForm):
#     contact=forms.CharField(
#         widget=forms.TextInput(
#             attrs={"class":"form-control"}
#         )
#     )

#     class Meta:
#         model=User
#         # fields=('contact')
#     def __init__ (self, *args, **kwargs):
#         super(SignupForm,self).__init__(*args,**kwargs)

#         self.fields['first_name'].widget.attrs['class']='form-control'
#         self.fields['last_name'].widget.attrs['class']='form-control'
#         self.fields['password1'].widget.attrs['class']='form-control'
#         self.fields['password2'].widget.attrs['class']='form-control'