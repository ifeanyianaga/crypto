import email
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from .models import AccountUser


#custom user create formm
class AccountCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = AccountUser
        fields = ['email','first_name','username']


    def clean_email(self):
        get_email=self.cleaned_data.get('email')
        email=get_email.lower()
        return email


    def clean_username(self):
        get_username=self.cleaned_data.get('username')
        username=get_username.lower()
        return username




    



    
       
        
        
        
       

   

#custom user change formm
class AccountChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = AccountUser
        fields = ('first_name','last_name')


    




class LoginForm(AuthenticationForm):
    class Meta:
        model = AccountUser
        fields = ["email","password"]


    def clean_email(self):
        get_email= self.cleaned_data.get('email')
        print(get_email)

   


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Email Address'})
        self.fields['password'].widget.attrs.update({'placeholder':"*************"})
       # self.fields['comment'].widget.attrs.update(size='40')
