from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from emr.views import *

router = DefaultRouter()

router.register(r'patient', PatientIdentityViewSet)
router.register(r'status', PatientStatusViewSet)
router.register(r'receptions', PatientListViewSet)
router.register(r'patient-registration', PatientListViewSet)
# router.register(r'')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('register_user/', CreateMedicalProfessional.as_view(), name='create_medical_person'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
