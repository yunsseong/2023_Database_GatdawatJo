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
    filterset_fields = ('patient_id',)
    
    # def perform_create(self, serializer):
    #     ins = serializer.save()
    #     reception_instance = PatientStatus(patient_id=ins.patient_id, patient_name=ins.patient_name, status="접수")
    #     reception_instance.save()

class PatientListViewSet(viewsets.ModelViewSet):
    queryset = PatientList.objects.all()
    serializer_class = PatientListSerializer

class ReceptionViewSet(viewsets.ModelViewSet):
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer
    filterset_fields = ('patient',)

    # def perform_create(self, serializer):
    #     print(self.request)
    #     serializer.save(patient = self.request.patient)

class MedicalPersonIdentityViewSet(viewsets.ModelViewSet):
    queryset = MedicalPersonIdentity.objects.all()
    serializer_class = MedicalPersonIdentitySerializer

class ChartViewSet(viewsets.ModelViewSet):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer
    filterset_fields = ('patient',)

class InspectViewSet(viewsets.ModelViewSet):
    queryset = Inspect.objects.all()
    serializer_class = InspectSerializer

class InspectTypeViewSet(viewsets.ModelViewSet):
    queryset = InspectType.objects.all()
    serializer_class = InspectTypeSerializer

class InbodyViewSet(viewsets.ModelViewSet):
    queryset = Inbody.objects.all()
    serializer_class = InbodySerializer

class BloodViewSet(viewsets.ModelViewSet):
    queryset = Blood.objects.all()
    serializer_class = BloodSerializer

class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializers_class = DiseaseSerializer

class TreatmentViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializers_class = TreatmentSerializer

class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializers_class = MedicationSerializer

class Image(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializers_class = ImageSerializer


