from django.db import models
import uuid

class PatientIdentity(models.Model):
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_name = models.CharField(max_length=60, null=False)
    patient_gender = models.CharField(max_length=1, blank=False, null=False)
    patient_birthday = models.DateField(null=False)
    patient_phone_number = models.CharField(max_length=15, blank=False, null=False)
    patient_main_address = models.TextField(blank=False, null=False)
    patient_detail_address = models.TextField(blank=False, null=False)
    patient_residence_number = models.CharField(max_length=8, blank=False, null=False)

    def __str__(self):
        return self.patient_name


class MedicalPersonIdentity(models.Model):
    medical_person_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    medical_person_name = models.CharField(max_length=60, null=False)
    medical_person_gender = models.CharField(max_length=1, blank=False, null=False)
    medical_person_birthday = models.DateField(null=False)
    medical_person_phone_number = models.CharField(max_length=15, null=True)
    medical_person_main_address = models.TextField(blank=False, null=False)
    medical_person_detail_address = models.TextField(blank=False, null=False)
    medical_person_license = models.TextField(blank=False, null=False)

class PatientInbody(models.Model):
    inbody_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.ForeignKey('PatientIdentity', on_delete=models.PROTECT)
    medical_person_id = models.ForeignKey('MedicalPersonIdentity', on_delete=models.PROTECT)
    weight = models.FloatField()
    muscle_mass = models.FloatField()
    body_fat_mass = models.FloatField()
    total_body_water = models.FloatField()
    protein = models.FloatField()
    minerals = models.FloatField()
    bmi = models.FloatField()
    percent_body_fat = models.FloatField()
    right_arm = models.FloatField()
    left_arm = models.FloatField()
    trunk = models.FloatField()
    right_leg = models.FloatField()
    left_leg = models.FloatField()
    ecw_ratio = models.FloatField()
    record_date = models.DateField()
    original_file_location = models.BinaryField()
