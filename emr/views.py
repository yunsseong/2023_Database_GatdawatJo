from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *

# class ViewSet(viewsets.ModelViewSet):
#     queryset = .objects.all()
#     serializer_class = Serializer

class PatientIdentityViewSet(viewsets.ModelViewSet):
    queryset = PatientIdentity.objects.all()
    serializer_class = PatientIdentitySerializer
    # def perform_create(self, serializer):
    #     ins = serializer.save()
    #     reception_instance = PatientStatus(patient_id=ins.patient_id, patient_name=ins.patient_name, status="접수")
    #     reception_instance.save()

class PatientListViewSet(viewsets.ModelViewSet):
    queryset = PatientList.objects.all()
    serializer_class = PatientListSerializer

class PatientReceptionViewSet(viewsets.ModelViewSet):
    queryset = PatientReception.objects.all()
    serializer_class = PatientReceptionSerializer

    # def perform_create(self, serializer):
    #     print(self.request)
    #     serializer.save(patient = self.request.patient)

class PatientStatusViewSet(viewsets.ModelViewSet):
    queryset = PatientStatus.objects.all()
    serializer_class = PatientStatusSerializer

class MedicalPersonIdentityViewSet(viewsets.ModelViewSet):
    queryset = MedicalPersonIdentity.objects.all()
    serializer_class = MedicalPersonIdentitySerializer

class PatientExaminationViewSet(viewsets.ModelViewSet):
    queryset = PatientExamination.objects.all()
    serializer_class = PatientExaminationSerializer

class PatientInbodyViewSet(viewsets.ModelViewSet):
    queryset = PatientInbody.objects.all()
    serializer_class = PatientInbodySerializer

class Image(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializers_class = ImageSerializer


