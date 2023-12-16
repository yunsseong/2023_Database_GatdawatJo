from rest_framework import serializers
from .models import CustomUser, MedicalProfessional, PatientIdentity, PatientInbody, MedicalPersonIdentity, PatientStatus, PatientList, PatientExamination,Image

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

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'name')  # CustomUser 모델의 필드 선택

class MedicalProfessionalSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()  # CustomUserSerializer를 MedicalProfessionalSerializer에 포함

    class Meta:
        model = MedicalPersonIdentity
        fields = ('medical_person_id', 'medical_person_system_id', 'medical_person_name', 'medical_person_gender', 'medical_person_birthday', 'medical_person_phone_number', 'medical_person_main_address', 'medical_person_license', 'classification_code')  # MedicalPersonIdentity 모델의 필드와 user 필드