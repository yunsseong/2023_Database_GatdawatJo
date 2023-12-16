from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from emr.views import *

router = DefaultRouter()

router.register(r'patients', PatientIdentityViewSet)
router.register(r'status', PatientStatusViewSet)
router.register(r'receptions', PatientReceptionViewSet)
router.register(r'list', PatientListViewSet)
router.register(r'patient-registration', PatientListViewSet)
router.register(r'chart', PatientChartViewSet)
router.register(r'inbody', PatientInbodyViewSet)
# router.register(r'')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
