from django.contrib.auth.models import User
from rest_framework import viewsets

from .models import Prisoner
from .serializers import UserSerializer, PrisonerSerializer


class UserViewSet(viewsets.ModelViewSet):
    '''Este viewset fornece automaticamente ações em 'list' e 'detail'.'''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PrisonerViewSet(viewsets.ModelViewSet):
    queryset = Prisoner.objects.all()
    serializer_class = PrisonerSerializer