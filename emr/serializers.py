from rest_framework import serializers
from .models import *

# class a(serializers.ModelSerializer):
#     class Meta:
#         model = a
#         fields = '__all__'
class PatientIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientIdentity
        fields = '__all__'

class PatientSpecificSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientIdentity
        fields = ['patient_id', 'patient_name', 'patient_gender']

class PatientReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientReception
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['patient'] = PatientIdentitySerializer(instance.patient).data
        return response

class PatientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientList
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['patient'] = PatientSpecificSerializer(instance.patient).data
        return response

class PatientStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientStatus
        field = '__all__'

class MedicalPersonIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalPersonIdentity
        fields = '__all__'

class PatientChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientChart
        fields = '__all__'

class InspectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspect
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['patient'] = PatientSpecificSerializer(instance.patient).data
        response['inspect'] = InspectTypeSerializer(instance.inspect_type_id).data
        return response

class InspectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectType
        field = '__all__'

class PatientInbodySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInbody
        fields = '__all__'

class PatientBloodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientBlood
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['patient'] = PatientSpecificSerializer(instance.patient).data
        return response

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = '__all__'