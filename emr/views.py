import base64
import os
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from .serializers import MedicalProfessionalSerializer
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.status import HTTP_200_OK
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from binascii import Error

# class ViewSet(viewsets.ModelViewSet):
#     queryset = .objects.all()
#     serializer_class = Serializer

class PatientIdentityViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = PatientIdentity.objects.all()
    serializer_class = PatientIdentitySerializer
    filterset_fields = ('patient_id',)
    
    # def perform_create(self, serializer):
    #     ins = serializer.save()
    #     reception_instance = PatientStatus(patient_id=ins.patient_id, patient_name=ins.patient_name, status="접수")
    #     reception_instance.save()

class PatientListViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = PatientList.objects.all()
    serializer_class = PatientListSerializer

class ReceptionViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer
    filterset_fields = ('patient_id',)

    # def perform_create(self, serializer):
    #     print(self.request)
    #     serializer.save(patient = self.request.patient)

class MedicalPersonIdentityViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = MedicalPersonIdentity.objects.all()
    serializer_class = MedicalPersonIdentitySerializer

    def retrieve(self, request, pk=None):
        try:
            token_key = request.headers['Authorization'].split(' ')[1]  # 토큰 추출
            token = Token.objects.get(key=token_key)  # 토큰으로 사용자 식별
            user = token.user

            # MedicalPersonIdentity와 request에서 추출한 사용자 비교
            medical_person_identity = MedicalPersonIdentity.objects.get(user=user)

            # 사용자와 MedicalPersonIdentity의 사용자가 일치하는 경우
            if medical_person_identity.user == request.user:
                serializer = self.serializer_class(medical_person_identity)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)  # 권한 없음
        except (KeyError, Token.DoesNotExist, MedicalPersonIdentity.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)

class ChartViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Chart.objects.all()
    serializer_class = ChartSerializer
    filterset_fields = ('patient_id',)


class InspectViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Inspect.objects.all()
    serializer_class = InspectSerializer

class InspectTypeViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = InspectType.objects.all()
    serializer_class = InspectTypeSerializer

class InbodyViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Inbody.objects.all()
    serializer_class = InbodySerializer
    filterset_fields = ('patient_id',)

class BloodViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Blood.objects.all()
    serializer_class = BloodSerializer

class DiseaseViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

class TreatmentViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer

class MedicationViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

class Image(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class CreateMedicalProfessional(APIView):
    def post(self, request):
        user_serializer = CustomUserSerializer(data=request.data['user'])
        medical_serializer = MedicalProfessionalSerializer(data=request.data)

        if user_serializer.is_valid() and medical_serializer.is_valid():
            # User 정보 저장
            user = user_serializer.save()
            # MedicalPersonIdentity 정보 저장
            medical_data = medical_serializer.validated_data
            medical_data['user'] = user  # 연결된 User 정보 추가
            MedicalPersonIdentity.objects.create(**medical_data)

            return Response(medical_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(medical_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # 요청에서 전달된 아이디와 비밀번호 가져오기
        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            # 아이디와 비밀번호 검증을 위해 인증 진행
            user = authenticate(username=username, password=password)

            if user:
                # 사용자가 인증되었다면 토큰 발행
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                # 인증 실패 시 오류 응답 반환
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # 아이디 또는 비밀번호가 전송되지 않은 경우 오류 응답 반환
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
