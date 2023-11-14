from rest_framework import serializers
from .models import PatientIdentity, PatientInbody
from .models import MedicalPersonIdentity

class PatientIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientIdentity
        fields = '__all__'

class MedicalPersonIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalPersonIdentity
        fields = '__all__'

class PatientInbodySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInbody
        fields = '__all__'
