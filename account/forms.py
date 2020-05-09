from django.forms import ModelForm
from . models import Order
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError



class CreateOrderForm(ModelForm):
    
    class Meta:
        model = Order
        fields = '__all__'



class UserRegisterForm(forms.Form):
    username = forms.CharField(label = "Username", max_length = 10, min_length = 4 )
    email = forms.EmailField(label = "Email")
    password1 = forms.CharField(label = "Password ", max_length = 8, min_length = 4 , widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Password ", max_length = 8, min_length = 4 , widget = forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower() #ensures that the username is always stored in lowercase
        check = User.objects.filter(username = username)

        # checking if username already exists in user database
        if check.count():
            raise ValidationError('this username is already taken')
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        check = User.objects.filter(email = email)
        
        if check.count():
            raise ValidationError('This Email already exists.')

        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password doesn't mactch.")

        return password2

    def save(self, commit = True):
        user =  User.objects.create_user(
            username = self.cleaned_data['username'],
            email = self.cleaned_data['email'],
            password = self.cleaned_data['password1'],
        )
        if commit : 
            user.save()

        return user

class UserLogin(forms.Form):
    username = forms.CharField(label = 'Username')
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput)
