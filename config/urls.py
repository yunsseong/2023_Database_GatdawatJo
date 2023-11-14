from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from emr.views import *

router = DefaultRouter()
router.register(r'patient', PatientIdentityViewSet)
router.register(r'medical/registration', MedicalPersonIdentityViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
