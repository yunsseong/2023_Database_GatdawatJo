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

class PatientIdentityViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = PatientIdentity.objects.all()
    serializer_class = PatientIdentitySerializer
    filterset_fields = ('patient_id',)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        decrypted_data = []
        for instance in queryset:
            # 암호화된 필드 복호화 작업
            decrypted_residence_number = decrypt_data(instance.patient_residence_number)


            response_data = {
                'patient_id': instance.patient_id,
                'patient_name': instance.patient_name,
                'patient_gender': instance.patient_gender,
                'patient_birth': instance.patient_birth,
                'patient_residence_number': decrypted_residence_number,
                'patient_phone_number': instance.patient_phone_number,
                'patient_emergency_phone_number': instance.patient_emergency_phone_number,
                'patient_address': instance.patient_address,
                'patient_agree_essential_term': instance.patient_agree_essential_term,
                'patient_agree_optional_term': instance.patient_agree_optional_term,

            }
            decrypted_data.append(response_data)

        return Response(decrypted_data, status=status.HTTP_200_OK)
    
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
    filterset_fields = ('patient', 'reception_id')

    # def perform_create(self, serializer):
    #     print(self.request)
    #     serializer.save(patient = self.request.patient)

class MedicalPersonIdentityViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = MedicalPersonIdentity.objects.all()
    serializer_class = MedicalPersonIdentitySerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            user = request.user  # 토큰을 통해 인증된 사용자

            # 사용자 정보를 기반으로 MedicalPersonIdentity를 조회
            medical_person_identity = MedicalPersonIdentity.objects.get(user=user)

            # MedicalPersonIdentity에서 필요한 정보를 직렬화하여 반환
            serializer = self.get_serializer(medical_person_identity)
            return Response(serializer.data)

        except MedicalPersonIdentity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ChartViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Chart.objects.all()
    serializer_class = ChartSerializer
    filterset_fields = ('patient', 'chart_id',)


class InspectViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Inspect.objects.all()
    serializer_class = InspectSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

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
    filterset_fields = ('patient',)

class BloodViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Blood.objects.all()
    serializer_class = BloodSerializer
    filterset_fields = ('patient',)

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

class PhysioViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = PatientPhysio.objects.all()
    serializer_class = PatientPhysioSerializer

class PhysioTypeViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = PhysioType.objects.all()
    serializer_class = PhysioTypeSerializer

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
