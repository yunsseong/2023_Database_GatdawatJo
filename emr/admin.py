from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(PatientIdentity)
admin.site.register(MedicalPersonIdentity)
admin.site.register(PatientExamination)
admin.site.register(PatientInbody)
admin.site.register(PatientXRay)
admin.site.register(PatientStatus)
admin.site.register(PatientList)
admin.site.register(Image)
admin.site.register(ClassificationCode)
