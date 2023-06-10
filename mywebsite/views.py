from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import gettext as _ 
from django.utils.translation import get_language,activate,gettext
from django.shortcuts import get_object_or_404, render,reverse,get_list_or_404
from django.http import HttpResponse
from requests import Session,Request
from django.contrib.auth.decorators import login_required
from account.models import AccountUser
from dashboard.models import Dashboard
from dashboard.forms import DepositForm,WithdrawForm,ProfitForm
from django.db.models import F
from django.core.mail import send_mail
from django.conf import settings
from contents.models import About,Crypto_logo,Feedback,Plan
from  requests import Session,Request 
import json
from django.contrib import messages

def index(request):
    trans=translate(language='fr')
    about=About.objects.all()
    logo=Crypto_logo.objects.all()
    feed=Feedback.objects.all()
    plans=Plan.objects.all()
    title=_("Home")
    """
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters ={'start':1,'limit':30,'sort':'market_cap','cryptocurrency_type':'all'}
    headers ={'Accepts':'application/json','X-CMC_PRO_API_KEY':'204cd731-3c5a-4fec-8024-c0aeaa0f998b'}
    session = Session()
    session.headers.update(headers)
    res = session.get(url,params=parameters)
    
    deserialized =json.loads(res.text)['data']
    """


    

    deserialized=" "
    template_name="homepage.html"
    context={"deserialized":deserialized,"about":about,"title":title,"logo":logo,"feed":feed,"plans":plans,"trans":trans}
    
    return render(request,template_name,context)

def translate(language):
    current_language=get_language()
    try:
        activate(language)
        text = gettext('home')
    finally:
        activate(current_language)
    return text


@login_required
def admin_dashboard(request):
    title="Admin Dashboard"
    if request.user.is_authenticated and request.user.is_staff:
        pending_list =Dashboard.objects.all()
        
        template_name="admin.html"
    else:
        return HttpResponseRedirect(reverse('home'))


    context={"pending_list":pending_list,"title":title}
    return render(request,template_name,context)
  




@login_required
def admin_detail(request,id):
    title="Confirm Deposit"
    obj = get_object_or_404(Dashboard,accountUser=id)
    
    if request.user.is_authenticated and request.user.is_staff:
    
      
        form =DepositForm(request.POST or None,instance=obj)
        if form.is_valid():
            item=form.save(commit=False)
            amount =form.cleaned_data.get('pending_deposit')
            
            item.pending_deposit=F('pending_deposit')-amount
            item.approved_deposit=F('approved_deposit')+amount
            item.balance=F('balance') + amount
            item.notification_deposit=0
            
    
            item.save(update_fields=['pending_deposit','balance','approved_deposit','notification_deposit'])
            history =obj.history_set.create(user=id,status=True,amount=amount,action="Deposit")
            history.save()
           
           

            form=DepositForm()
            text=f"Withdrawal successfully received ,you would be notified the moment it is processed"
            messages.success(request,text)
    
    button="Deposit"
    activity="DEPOSIT"           
    context={"obj":obj,"form":form,"button":button,"activity":activity,"title":title}
    template_name ="detail.html"
        
    
    return render(request,template_name,context)





 
@login_required
def pending_withdrawal(request,id):
    title="Confirm Withdrawal"
    obj = get_object_or_404(Dashboard,accountUser=id)
    if request.user.is_authenticated and request.user.is_staff:
    
      
        form =WithdrawForm(request.POST or None,instance=obj)
        if form.is_valid():
            item=form.save(commit=False)
            amount =form.cleaned_data.get('pending_withdrawal')
            if amount > item.balance:
                item.pending_withdrawal=item.pending_withdrawal-amount
                withdrawable=amount - item.balance

                the_balance=amount-withdrawable
                item.profit=item.profit-withdrawable
                print(item.profit)
                print(item.balance)
                print(the_balance)

                item.balance=item.balance-the_balance
                print(item.balance)
                
                
                item.approved_withdrawal=F('approved_withdrawal')+amount

                item.save(update_fields=['pending_withdrawal','balance','approved_withdrawal','notification_withdrawal','profit'])
            else:

                item.pending_withdrawal=F('pending_withdrawal')-amount
                item.approved_withdrawal=F('approved_withdrawal')+amount
                item.balance=F('balance') - amount
                item.notification_withdrawal=0
    
                item.save(update_fields=['pending_withdrawal','balance','approved_withdrawal','notification_withdrawal','profit'])
            history =obj.history_set.create(user=id,status=True,amount=amount,action="Withdrawal")
            history.save()
           

            form=WithdrawForm()
            text=f"Withdrawal successfully received ,you would be notified the moment it is processed"
            messages.success(request,text)
    
    button="Withdraw"
    activity="WITHDRAWAL"     
    context={"obj":obj,"form":form,"button":button,"activity":activity,"title":title}
    template_name ="detail.html"
        
    
    return render(request,template_name,context)


@login_required
def investor_earnings(request):
    
    if request.user.is_authenticated and request.user.is_staff:

        list_of_users=Dashboard.objects.all()
        template_name="profit.html"

    else:
        return HttpResponseRedirect(reverse('home'))
   
    context={"list_of_users":list_of_users}
    return render(request,template_name,context)



@login_required
def add_profit(request,id):
    button="Add"
    title="Add Earnings"
    obj = get_object_or_404(Dashboard,accountUser=id)
    if request.user.is_authenticated and request.user.is_staff:
        form=ProfitForm(request.POST or None,instance=obj)
        if form.is_valid():
            item=form.save(commit=False)
            amount=form.cleaned_data.get('profit')
            item.profit=F('profit')+amount
            item.save(update_fields=['profit'])
            form=ProfitForm()
        

            pass
        template_name="add_profit.html"
        
    else:
        return HttpResponseRedirect(reverse('home'))
    context={"form":form,"button":button,"title":title}
   
    return render(request,template_name,context)
   



@login_required
def reset(request):
    title="Reset"
    if request.user.is_authenticated and request.user.is_staff:
        pending_list=Dashboard.objects.all()
        template_name="reset.html"
    else:
        return HttpResponseRedirect(reverse('home'))
    
    context={"title":title,"pending_list":pending_list}
    return render(request,template_name,context)



@login_required
def reset_detail(request,id):
    title="Reset Pending deposit"
    button="Clear"
    obj = get_object_or_404(Dashboard,accountUser=id)
    if request.user.is_authenticated and request.user.is_staff:
        form =DepositForm(request.POST or None,instance=obj)
        if form.is_valid():
            item=form.save(commit=False)
            amount=form.cleaned_data.get('pending_deposit')
            item.pending_deposit=F('pending_deposit')-amount
            item.notification_deposit=0
            item.save(update_fields=['pending_deposit','notification_deposit'])
            return HttpResponseRedirect(reverse('reset'))
    
            
        template_name="reset-detail.html"
        pass
    else:
        return HttpResponseRedirect(reverse('home'))
    context={"title":title,"form":form,"button":button,"obj":obj}
    return render(request,template_name,context)

  




