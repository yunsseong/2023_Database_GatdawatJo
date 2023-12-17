from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

admin.site.register(PatientIdentity)
admin.site.register(MedicalPersonIdentity)
admin.site.register(Chart)
admin.site.register(Inbody)
admin.site.register(Reception)
admin.site.register(XRay)
admin.site.register(PatientList)
admin.site.register(Image)
admin.site.register(ClassificationCode)
admin.site.register(Inspect)
admin.site.register(InspectType)
admin.site.register(Disease)
admin.site.register(Medication)
admin.site.register(Treatment)
admin.site.register(Blood)
admin.site.register(Physio)
admin.site.register(Reservation)