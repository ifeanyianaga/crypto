
from django import forms
from account.models import AccountUser

from . models import Dashboard
from django.utils.translation import gettext_lazy as _
from django.forms import Widget


class DepositForm(forms.ModelForm):
    class Meta:
        model=Dashboard
        fields=['pending_deposit','tokens']
        #widgets={
           # 'pending_deposit':forms.NumberInput(attrs={'class':'form-control','type':'number'}),
           # 'tokens':forms.Select(attrs={'class':'form-control'})
        #}


    def clean_pending_deposit(self,*args,**kwargs):
        instance=self.instance
        user=AccountUser.objects.get(email=instance)
        pending_deposit=self.cleaned_data.get('pending_deposit')
        dash=Dashboard.objects.get(accountUser=user)
        comparator=dash.comparator
        if pending_deposit < comparator:
            raise forms.ValidationError("Minimum deposit is 1 USD")
    
        return pending_deposit

    
  


class WithdrawForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields =['wallet_address','tokens','pending_withdrawal']
        widgets={
            'wallet_address':forms.TextInput(attrs={'class':'form-control notice','type':'text',"placeholder":'Enter or paste the address'}),
            'tokens':forms.Select(attrs={'class':'form-control notice'}),
            #'network':forms.Select(attrs={'class':'form-control notice'})
    }
      


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pending_withdrawal'].widget.attrs.update({'id':'withdraw','placeholder':'Enter or paste the address'})
       
       
            


    def clean_pending_withdrawal(self,*args,**kwarags):
        instance=self.instance
        pending_withdrawal= self.cleaned_data.get('pending_withdrawal')
        user=AccountUser.objects.get(email=instance)
        qs =Dashboard.objects.get(accountUser=user)
        profit =qs.profit
        balance = qs.balance + profit
        #balance = balance * 0.90

        if pending_withdrawal > balance:
            raise forms.ValidationError("Insufficient Funds")

        if pending_withdrawal < qs.comparator:
            raise forms.ValidationError("You cannot withdraw less than 1 USD")

        
        return pending_withdrawal

       
class ProfitForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields =['profit']
        widgets={
            'wallet_address':forms.TextInput(attrs={'class':'form-control notice','type':'text',"placeholder":'Enter or paste the address'}),
            'tokens':forms.Select(attrs={'class':'form-control notice'}),
            #'network':forms.Select(attrs={'class':'form-control notice'})
    }

     

        
        
        


      




       

 