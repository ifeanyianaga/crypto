
from django.db import models
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField
from account.models import AccountUser
from django.db.models.signals import post_save
from django import forms
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator 
from django.core.validators import MinValueValidator, MaxValueValidator
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw 




class Dashboard(models.Model):
  CRYPTO_TOKENS = (
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
        ('USDT','Tether'),
        ('BNB', 'BNB')
    )

  NETWORK = (
        ('BTC', 'BTC'),
        ('TRC20', 'TRC20'),
        ('KCC','KCC'),
        ('ARBITRUM', 'ARBITRUM')
    )


  notify_user_timestamp=models.DateTimeField(auto_now_add=True)
  pending_deposit = MoneyField(max_digits=14, decimal_places=2, default_currency='USD',blank=False,null=False,verbose_name="Deposit Amount",default=0.0,  validators=[MinMoneyValidator(1)])
  tokens= models.CharField(max_length=4, choices=CRYPTO_TOKENS,default='BTC')
  #network= models.CharField(max_length=8, choices=NETWORK,default='BTC')
  comparator= MoneyField(max_digits=14, decimal_places=2, default_currency='USD',blank=False,null=False,verbose_name="comparator",default=1.0, validators=[MinMoneyValidator(1),MaxMoneyValidator(1)],)
  accountUser = models.OneToOneField(AccountUser,on_delete=models.CASCADE,verbose_name="User",primary_key=True)
  #earnings = MoneyField(max_digits=14, decimal_places=2, default_currency='USD',blank=False,null=False,default=0.0, validators=[MinMoneyValidator(1)])
  balance = MoneyField(max_digits=19, decimal_places=2, default_currency='USD',blank=False,null=False,verbose_name="Balance",default=0.0, validators=[MinMoneyValidator(0)])
  approved_deposit = MoneyField(max_digits=19, decimal_places=2, default_currency='USD',blank=False,null=False,verbose_name="Approved Deposit",default=0.0, validators=[MinMoneyValidator(1)])
  approved_withdrawal = MoneyField(max_digits=19, decimal_places=2, default_currency='USD',blank=False,null=False,verbose_name="Aprroved_withdrawal",default=0.0, validators=[MinMoneyValidator(1)])
  date =models.DateTimeField(auto_now_add=True)
  phone = PhoneNumberField(blank=True)
  pending_withdrawal = MoneyField(max_digits=14, decimal_places=2, default_currency='USD',blank=False,null=False,verbose_name="Withdrawal Amount",default=0.0, validators=[MinMoneyValidator(1)])
  profit = MoneyField(max_digits=14, decimal_places=2, default_currency='USD',blank=True,null=True,verbose_name="Profit",default=0.0, validators=[MinMoneyValidator(1)])
  notification_deposit =models.PositiveSmallIntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(1)])
  notification_withdrawal =models.PositiveSmallIntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(1)])
  wallet_address=models.CharField(max_length=300)



  def __str__(self):
    return str(self.accountUser)

 





class History(models.Model):
  user=models.ForeignKey(Dashboard,on_delete=models.CASCADE)
  status =models.BooleanField(default=False)
  amount = MoneyField(max_digits=19, decimal_places=2, default_currency='USD',blank=True,null=True,verbose_name="Amount",)
  action = models.CharField(max_length=100,verbose_name="Action",null=True,blank=True)
  
  date =models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return str(self.user)




class Address(models.Model):
  wallet_address=models.CharField(max_length=400,verbose_name='Wallet Address',null=True,blank=True)
  logo=models.FileField(blank=True,null=True,upload_to="images/")
  token=models.CharField(max_length=200)
  qr_code=models.ImageField(upload_to="images/",null=True,blank=True)

  def __str__(self):
    return self.token

  def save(self,*args,**kwargs):
    qrcode_img=qrcode.make(self.wallet_address)
    canvas=Image.new('RGB',(370,370), 'white')
    draw=ImageDraw.Draw(canvas)
    canvas.paste(qrcode_img)
    fname=f"qr_code-{self.token}.png"
    buffer=BytesIO()
    canvas.save(buffer,'PNG')
    self.qr_code.save(fname,File(buffer),save=False)
    canvas.close()
    super().save(*args,**kwargs)


  


  

  