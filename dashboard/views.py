

from django import forms
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,reverse,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Dashboard,Address
from account.models import AccountUser
from  requests import Session,Request 
import json 
from .forms import DepositForm, WithdrawForm
from django.db.models import F
from django.utils import timezone
from django.core.mail import send_mail
from datetime import date
import time
import datetime
from django.conf import settings
from django.contrib import messages





# Create your views here.

@login_required   
def dashboard(request):
    title="Dashboard"
    
    
  
    data = request.user
    user = get_object_or_404(AccountUser,email =data.email)
    
    obj = get_object_or_404(Dashboard,accountUser=user.id)
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters ={'start':1,'limit':100,'sort':'market_cap','cryptocurrency_type':'all'}
    headers ={'Accepts':'application/json','X-CMC_PRO_API_KEY':'204cd731-3c5a-4fec-8024-c0aeaa0f998b'}
    session = Session()
    session.headers.update(headers)
    res = session.get(url,params=parameters)
    
    deserialized =json.loads(res.text)['data']
    btc_price=json.loads(res.text)['data'][0]['quote']['USD']['price']
    
    
    balance=obj.balance
    

    btc=balance/btc_price
    

    
    
    context={'obj':obj,
        'user':user,'deserialized':deserialized,'balance':balance,'btc':btc,"title":title
    }
    template_name = "dashboard/index.html"
    return render(request,template_name,context)


@login_required
def withdraw(request):
    title="Withdraw"
    myUser = get_object_or_404(AccountUser,email=request.user.email)
    
  
    obj = get_object_or_404(Dashboard,accountUser=request.user.id)
    if obj.accountUser!=request.user:
        raise Http404
    form = WithdrawForm(request.POST or None,instance=obj)
    if form.is_valid():
        item=form.save(commit=False)
        depo=item.pending_withdrawal
        com=item.comparator
        item.notification_withdrawal=1
        notification=item.notification_withdrawal
        item.save()
       
        form = WithdrawForm()
        text=f"Withdrawal successfully received ,you would be notified the moment it is processed"
        messages.success(request,text)
        
        
        
        
  
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters ={'start':1,'limit':100,'sort':'market_cap','cryptocurrency_type':'all'}
    headers ={'Accepts':'application/json','X-CMC_PRO_API_KEY':'204cd731-3c5a-4fec-8024-c0aeaa0f998b'}
    session = Session()
    session.headers.update(headers)
    res = session.get(url,params=parameters)
    
    deserialized =json.loads(res.text)['data']

    btc_price=json.loads(res.text)['data'][0]['quote']['USD']['price']
    balance=obj.balance
    btc=balance/btc_price

    
    
    
    #deserialized =" "
    template_name ="dashboard/withdraw.html"
    get_obj=get_object_or_404(Dashboard,accountUser=myUser.id)
    pending= get_obj.pending_withdrawal
    balance =get_obj.balance
    wallet_address=obj.wallet_address
    
    profit =get_obj.profit
    total =profit + balance
    approved =get_obj.approved_withdrawal
    Action="Transaction"
    history=get_obj.history_set.exclude(action="Deposit")
    context ={'deserialized':deserialized,'form':form,'pending':pending,'approved':approved,'get_obj':get_obj,"Action":Action,"wallet_address":wallet_address,"balance":balance,"history":history,'btc':btc,"title":title,'profit':profit,'total':total}
    return render(request,template_name,context)
   










@login_required
def deposit(request):
    
    myUser = get_object_or_404(AccountUser,email=request.user.email)
    #address=get_object_or_404(Address)
  
    obj = get_object_or_404(Dashboard,accountUser=request.user.id)
    if obj.accountUser!=request.user:
        raise Http404
    form = DepositForm(request.POST or None,instance=obj)
    if form.is_valid():
        item=form.save(commit=False)

    
    

        depo=item.pending_deposit
        com=item.comparator
        item.notification_deposit=1
        year=datetime.date.today().strftime("%Y")
        month=datetime.date.today().strftime("%B")
        day =datetime.date.today().strftime("%A")
        date=datetime.date.today().strftime("%d")

        time=datetime.datetime.now().time()
        now= f'{day},{month} {date}, {year}\n\n\n{time}'
    
        subject='Deposit Initialized'
        name=request.user.first_name
    
        message=f"Hello {name},\n\n Please be informed that your digital dashboard was\n accessed on:\n\n\n {now},\n\n And a Deposit of {depo} was initialized. \n\n\n Stay Safe."
        email=request.user.email
        #send_mail(subject,message,settings.EMAIL_HOST_USER,[email],fail_silently=False)
        
        item.save()
       
        form = DepositForm()
       
        
        
        
        
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters ={'start':1,'limit':100,'sort':'market_cap','cryptocurrency_type':'all'}
    headers ={'Accepts':'application/json','X-CMC_PRO_API_KEY':'204cd731-3c5a-4fec-8024-c0aeaa0f998b'}
    session = Session()
    session.headers.update(headers)
    res = session.get(url,params=parameters)
    
    deserialized =json.loads(res.text)['data']
    btc_price=json.loads(res.text)['data'][0]['quote']['USD']['price']
    balance=obj.balance
    btc=balance/btc_price
    
   
    
    #deserialized =" "
    template_name ="dashboard/deposit.html"
    get_obj=get_object_or_404(Dashboard,accountUser=myUser.id)
    pending= get_obj.pending_deposit 
    history=get_obj.history_set.exclude(action="Withdrawal")
    
    approved =get_obj.approved_deposit
    balance=get_obj.balance
    Action="Transaction"
    tokens=get_obj.tokens
    wallet=Address.objects.filter(token=tokens)[:1]
    profit =get_obj.profit
    total =profit + balance


    context ={'profit':profit,'total':total,'deserialized':deserialized,'form':form,'pending':pending,'approved':approved,'get_obj':get_obj,"Action":Action,"balance":balance,"history":history,"wallet":wallet,'btc':btc}
    return render(request,template_name,context)
    




def transactions(request):
    myUser = get_object_or_404(AccountUser,email=request.user.email)
    #address=get_object_or_404(Address)
  
    obj = get_object_or_404(Dashboard,accountUser=request.user.id)
    if obj.accountUser!=request.user:
        raise Http404
    user=AccountUser.objects.get(email=request.user.email)
    get_obj=get_object_or_404(Dashboard,accountUser=user.id)
    history =get_obj.history_set.all()
    balance=obj.balance
    template_name="dashboard/transactions.html"
    context={'history':history,"balance":balance}
    return render(request,template_name,context)


@login_required
def settings(request):
    myUser = get_object_or_404(AccountUser,email=request.user.email)
    #address=get_object_or_404(Address)
  
    obj = get_object_or_404(Dashboard,accountUser=request.user.id)
    if obj.accountUser!=request.user:
        raise Http404

    #myUser = get_object_or_404(AccountUser,email=request.user.email)
    
  
    obj = get_object_or_404(Dashboard,accountUser=request.user.id)
    balance=obj.balance
    context={"balance":balance}
    template_name="dashboard/settings.html"
    return render(request,template_name,context)





