import email
from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.contrib.auth.models import User



# Create your models here.
class AccountUser(AbstractUser):
    email = models.EmailField(verbose_name="Email Address",unique=True)
    country = CountryField(blank_label='Select a country/region of residence',null=False,blank=True)



   
 

  


    



    USERNAME_FIELD ="email"
    REQUIRED_FIELDS = ["username"]
