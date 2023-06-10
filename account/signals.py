from django.db.models.signals import post_save
from dashboard.models import Dashboard
from .models import AccountUser
from django.core.mail import send_mail
from django.contrib.auth import user_logged_in
from django.utils import timezone
from django.conf import settings
from datetime import date
import time
import datetime


def create_dashboard(sender,instance,created,**kwargs):
  if created:
    Dashboard.objects.create(accountUser=instance)
    #theMessage ="Dear ,"+ instance.get_full_name() +"\n you have successfully created an account with us"
   
    
    #send_mail( 'Account creation successful', theMessage, 'binadesign23@gmail.com', [instance.email], fail_silently=False, )
    #print("email sent successfully")
    print("dashboard created")
  

post_save.connect(create_dashboard,sender=AccountUser)


def update_dashboard(sender,instance,created,**kwargs):
    if created == False:
      Dashboard.objects.get_or_create(accountUser=instance)
      
      instance.dashboard.save()
    
     
      
      print("profile updated")

post_save.connect(update_dashboard,sender=AccountUser)
"""
def notify_login(sender,request,user,**kwargs):
  if user is not None and request.user.is_authenticated:
    year=datetime.date.today().strftime("%Y")
    month=datetime.date.today().strftime("%B")
    day =datetime.date.today().strftime("%A")
    date=datetime.date.today().strftime("%d")

    time=datetime.datetime.now().time()
    now= f'{day},{month} {date}, {year}\n\n\n{time}'
    
    subject='Login Confirmation'
    name=request.user.first_name
    
    message=f"Hello {name},\n\n Please be informed that your digital dashboard was\n accessed on:\n\n\n {now},\n\n You are advised to always keep your login details safe \n\n and never disclose it to anyone. \n\n\n Stay Safe."
    email=request.user.email
    send_mail(subject,message,settings.EMAIL_HOST_USER,[email],fail_silently=False)
    print("email sent")
   

user_logged_in.connect(notify_login,sender=AccountUser)
"""
