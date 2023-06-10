from rest_framework import viewsets
from .serializers import AccountUserSerializer
from account.models import AccountUser


class AccountUserView(viewsets.ModelViewSet):
    queryset = AccountUser.objects.all()
    serializer_class = AccountUserSerializer    

