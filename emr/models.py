from django.db import models
import uuid

from django.db.models import TextChoices


class PatientIdentity(models.Model):
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_name = models.CharField(max_length=60, null=False)
    patient_gender = models.CharField(max_length=1, blank=False, null=False)
    patient_birthday = models.DateField(blank=False, null=False)
    patient_phone_number = models.CharField(max_length=15, blank=False, null=False)
    patient_main_address = models.TextField(blank=False, null=False)
    patient_detail_address = models.TextField(blank=False, null=False)
    patient_residence_number = models.CharField(max_length=8, blank=False, null=False)

    class Meta:
        db_table = 'patient_identity'
    def __str__(self):
        return self.patient_name

class ClassificationCode(models.Model):
    classification_code = models.CharField(max_length=5, primary_key=True, blank=False, null=False)
    classification_name = models.CharField(max_length=20, blank=False, null=False)

class MedicalPersonIdentity(models.Model):
    medical_person_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    medical_person_system_id = models.CharField(max_length=20, blank=False, null=False)
    medical_person_system_pw = models.CharField
    medical_person_name = models.CharField(max_length=60, blank=False, null=False)
    medical_person_gender = models.CharField(max_length=1, blank=False, null=False)
    medical_person_birthday = models.DateField(blank=False, null=False)
    medical_person_phone_number = models.CharField(max_length=15, blank=False, null=False)
    medical_person_main_address = models.TextField(blank=False, null=False)
    medical_person_detail_address = models.TextField(blank=False, null=False)
    medical_person_license = models.TextField(blank=False, null=False)
    classification_code = models.ForeignKey('ClassificationCode', on_delete=models.PROTECT)

    class Meta:
        db_table = 'medical_person_identity'


class PatientExamination(models.Model):
    examination_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.ForeignKey(PatientIdentity, on_delete=models.CASCADE)
    medical_person_id = models.ForeignKey(MedicalPersonIdentity, on_delete=models.PROTECT)
    examination_detail = models.TextField()
    examination_datetime = models.DateTimeField()

    class Meta:
        db_table = 'patient_examination'


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

    class Meta:
        db_table = 'patient_inbody'
class PatientXRay(models.Model):
    xray_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.ForeignKey(PatientIdentity, on_delete=models.CASCADE)
    medical_person_id = models.ForeignKey(MedicalPersonIdentity, on_delete=models.PROTECT)
    shooting_timestamp = models.DateTimeField()
    original_xray_location = models.BinaryField()

    class Meta:
        db_table = 'patient_xray'

class PatientStatus(models.Model):
    class Status(TextChoices):
        RECEPTION = "reception", "접수"
        EXAMINATION = "examination", "진료"
        TREATMENT = "treatment", "치료"
        PHYSIOTHERAPY = "physiotherapy", "물리치료"
        PURCHASE = "purchase", "수납"

    status_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.ForeignKey(PatientIdentity, on_delete=models.CASCADE)
    status = models.CharField(choices=Status.choices, max_length=15)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'patient_status'