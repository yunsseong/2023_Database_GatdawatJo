from rest_framework import serializers
from cryptography.fernet import Fernet
from .models import *
import base64

class PatientIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientIdentity
        fields = '__all__'

    def create(self, validated_data):
        residence_number = validated_data.get('patient_residence_number')
        encrypted_residence_number = encrypt_data(residence_number)
        validated_data['patient_residence_number'] = encrypted_residence_number
        return super().create(validated_data)

def encrypt_data(data):
    key = settings.RESIDENCE_KEY

    cipher_suite=Fernet(key)
    encrypt_data = cipher_suite.encrypt(data.encode('utf-8')).decode('utf-8')

    return encrypt_data

def decrypt_data(encrypted_data):
    key = settings.RESIDENCE_KEY

    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data.encode('utf-8')).decode('utf-8')

    return decrypted_data

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
        return response

    def to_internal_value(self, data):
        # 'disease', 'inspect', 'treatment', 'medication' 필드를 처리하여 단일 값으로 변경
        for field_name in ['disease', 'inspect', 'treatment', 'medication']:
            field_value = data.get(field_name)
            if isinstance(field_value, list) and len(field_value) == 1:
                data[field_name] = field_value[0]  # 리스트 안에 한 개 값이면 해당 값을 단일 값으로 변경
        return super().to_internal_value(data)

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

class PatientPhysioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientPhysio
        fields = '__all__'

    def to_representation(self, instance):
            response = super().to_representation(instance)
            response['physio_type'] = PhysioTypeSerializer(instance.physio_type).data
            return response

class PhysioTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysioType
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['patient'] = PatientSpecificSerializer(instance.patient).data
        return response

class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name')  # CustomUser 모델의 필드 선택

class MedicalProfessionalSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()  # CustomUserSerializer를 MedicalProfessionalSerializer에 포함

    class Meta:
        model = MedicalPersonIdentity
        fields = ('medical_person_id', 'medical_person_system_id', 'medical_person_name', 'medical_person_gender', 'medical_person_birthday', 'medical_person_phone_number', 'medical_person_main_address', 'medical_person_license', 'classification_code')  # MedicalPersonIdentity 모델의 필드와 user 필드