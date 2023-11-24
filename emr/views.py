from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *

class PatientIdentityViewSet(viewsets.ModelViewSet):
    queryset = PatientIdentity.objects.all()
    serializer_class = PatientIdentitySerializer

class MedicalPersonIdentityViewSet(viewsets.ModelViewSet):
    queryset = MedicalPersonIdentity.objects.all()
    serializer_class = MedicalPersonIdentitySerializer

class PatientInbodyViewSet(viewsets.ModelViewSet):
    queryset = PatientInbody.objects.all()
    serializer_class = PatientInbodySerializer
