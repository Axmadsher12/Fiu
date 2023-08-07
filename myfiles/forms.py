from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

class UserCreateForm(UserCreationForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"mail_text","placeholder":"Username","type":"text"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"mail_text","placeholder":"Email","type":"email"}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={"class":"mail_text","placeholder":"Enter password","type":"password"}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={"class":"mail_text","placeholder":"Confirm password","type":"password"}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class Subscribe_Newsletter_Form(ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    Your_email = forms.CharField(widget=forms.TextInput(attrs={"Name":"Subscribe Newsletter","class":"email_text","placeholder":"Enter Your Email","type":"email"}))
    class Meta:
        model = Subscribe_Newsletter
        fields = ['Your_email']

class Mail_Message_Form(ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    Title = forms.CharField(widget=forms.TextInput(attrs={"Name":"Mail Message","class":"mail_text","placeholder":"Title","type":"text", 'name':"Title"}))
    Message = forms.CharField(widget=forms.Textarea(attrs={"Name":"Message","class":"massage-bt","placeholder":"Message",'rows':"5", 'id':"comment", 'name':"Massage"}))
    class Meta:
        model = Mail_Message
        fields = ['Title','Message']