from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from emr.views import *

router = DefaultRouter()

router.register(r'patients', PatientIdentityViewSet)
router.register(r'receptions', ReceptionViewSet)
router.register(r'list', PatientListViewSet)
router.register(r'chart', ChartViewSet)
router.register(r'inbody', InbodyViewSet)
router.register(r'blood', BloodViewSet)
router.register(r'medication', MedicationViewSet)
router.register(r'inspect', InspectViewSet)
router.register(r'inspect_type', InspectTypeViewSet)
router.register(r'disease', DiseaseViewSet)
router.register(r'treatment', TreatmentViewSet)
router.register(r'medical', MedicalPersonIdentityViewSet)
router.register(r'physio', PhysioViewSet)
router.register(r'physio_type', PhysioTypeViewSet)
router.register(r'reservation', ReservationViewSet)
# router.register(r'')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('register_user/', CreateMedicalProfessional.as_view(), name='create_medical_person'),
    path('api/medical-info/', MedicalPersonInfoView.as_view(), name='medical-info'),
    path('api/token/', CustomAuthToken.as_view(), name='custom_token_obtain'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
