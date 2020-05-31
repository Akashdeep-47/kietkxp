from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import UserProfile
from django.core.validators import RegexValidator



class UserRegisterForm(UserCreationForm):
    email= forms.EmailField(validators=[RegexValidator(regex='^[a-z0-9]+\.[a-z0-9]{10,}@[kiet]+\.[edu]{3}$',
                                     message='Please enter a valid KIET email id',code='Invalid')])
    first_name= forms.CharField(max_length=25,validators=[RegexValidator(regex='^[a-zA-Z]{3,}$',
                                     message='Please enter a valid First name',code='Invalid')])
    last_name= forms.CharField(max_length=25,validators=[RegexValidator(regex='^[a-zA-Z]{3,}$',
                                     message='Please enter a valid Last name',code='Invalid')])



    class Meta:
        model= User
        fields= ['first_name','last_name','username','email','password1','password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model= UserProfile
        fields= ['branch','mobile_number']
