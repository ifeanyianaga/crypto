from django.urls import path
from . import views


urlpatterns =[

path('',views.dashboard,name="dashboard"),
path('deposit/',views.deposit,name="deposit"),
path('withdraw/',views.withdraw,name="withdraw"),
path('transactions/',views.transactions,name='transactions'),
path('settings/',views.settings,name="settings"),



]
