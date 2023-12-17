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

class ReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reception
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

class MedicalPersonIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalPersonIdentity
        fields = '__all__'

class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chart
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['patient'] = PatientIdentitySerializer(instance.patient).data
        response['medical'] = MedicalPersonIdentitySerializer(instance.medical).data
        return response

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
        fields = '__all__'

class InbodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inbody
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['patient'] = PatientIdentitySerializer(instance.patient).data
        return response

class BloodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blood
        fields = '__all__'

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['patient'] = PatientSpecificSerializer(instance.patient).data
    #     return response

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
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

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'name')  # CustomUser 모델의 필드 선택

class MedicalProfessionalSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()  # CustomUserSerializer를 MedicalProfessionalSerializer에 포함

    class Meta:
        model = MedicalPersonIdentity
        fields = ('medical_person_id', 'medical_person_system_id', 'medical_person_name', 'medical_person_gender', 'medical_person_birthday', 'medical_person_phone_number', 'medical_person_main_address', 'medical_person_license', 'classification_code')  # MedicalPersonIdentity 모델의 필드와 user 필드