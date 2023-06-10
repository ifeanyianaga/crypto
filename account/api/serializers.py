from rest_framework import serializers
from account.models import AccountUser
from django_countries.serializer_fields import CountryField

class AccountUserSerializer(serializers.ModelSerializer):
    country= CountryField()

    class Meta:
        model = AccountUser
        fields ='__all__'
       # read_only_fields = ['countries']
       
