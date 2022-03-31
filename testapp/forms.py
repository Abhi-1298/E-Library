
from django import forms
from .models import EbookModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,UserChangeForm
from django.utils.translation import  gettext_lazy as _


""" UserCreationForm,AuthenticationForm,UserChangeForm  all these are django builtin-forms and inherit those forms for making custom profile and customuser by overriding the form  fields"""
class EbookModelForm(forms.ModelForm):
    class Meta:
        model = EbookModel
        fields = ['title','author','publisher','year','cover','books_pdf']



# XXX creating auth sys using builtinForms
class SignupForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={"class": 'form-control','style':'width:300px'}))  
    password2 = forms.CharField(label="Password(Again)", widget=forms.PasswordInput(
        attrs={"class": 'form-control','style':'width:300px'}))  
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':"First Name",'last_name':'Last Name','email':'Email'}

        # bootstrap widgets and inside attrinbutes any css properties you can take
        widgets = {'username':forms.TextInput(attrs={"class": 'form-control','style':'width:300px'}),
                    'first_name':forms.TextInput(attrs={"class": 'form-control','style':'width:300px'}),
                    'last_name':forms.TextInput(attrs={"class": 'form-control','style':'width:300px'}),
                    'email':forms.TextInput(attrs={"class": 'form-control','style':'width:300px'}), 
        }




# profile  and whole data of profile came from user model in frontend
class UserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':"First Name",'last_name':'Last Name','email':'Email'}





class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control','style':'width:300px'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete':'current-password', 'class':'form-control','style':'width:300px'}))  # form-control for bootstrap




