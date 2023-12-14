from rest_framework import serializers
from .models import PatientIdentity, PatientInbody, MedicalPersonIdentity, PatientStatus, PatientList, PatientExamination,Image, PatientReception

# class a(serializers.ModelSerializer):
#     class Meta:
#         model = a
#         fields = '__all__'
class PatientIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientIdentity
        fields = '__all__'

class PatientIdNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientIdentity
        fields = ['patient_id', 'patient_name']

class PatientReceptionSerializer(serializers.ModelSerializer):
    patient_id = PatientIdentitySerializer()
    class Meta:
        model = PatientReception
        fields = '__all__'

class PatientListSerializer(serializers.ModelSerializer):
    patient_id = PatientIdNameSerializer()
    class Meta:
        model = PatientList
        fields = '__all__'

class PatientStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientStatus
        field = '__all__'

class MedicalPersonIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalPersonIdentity
        fields = '__all__'

class PatientExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientExamination
        fields = '__all__'

class PatientInbodySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInbody
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = '__all__'