from django.db import models
import uuid

from django.db.models import TextChoices


class PatientIdentity(models.Model):
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_name = models.CharField(max_length=60, null=False)
    patient_gender = models.CharField(max_length=1, blank=False, null=False)
    patient_birthday = models.DateField(blank=False, null=False)
    patient_residence_number = models.CharField(max_length=8, blank=False, null=False)
    patient_phone_number = models.CharField(max_length=15, blank=False, null=False)
    patient_emergency_phone_number = models.CharField(max_length=15)
    patient_address = models.CharField(max_length=100)

    class Meta:
        db_table = 'patient_identity'

    def __str__(self):
        return self.patient_name

class PatientReception(models.Model):
    reception_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey('PatientIdentity', on_delete=models.CASCADE, related_name="patient",  default="")
    visit_reason = models.TextField(blank=False, null=False)
    reception_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'patient_reception'


class PatientList(models.Model):
    class type(TextChoices):
        NOMAL = "일반환자", "일반환자"
        EMERGENCY = "중증환자", "중증환자"
        VIP = "VIP", "VIP"

    patient_id = models.ForeignKey('PatientIdentity', on_delete=models.CASCADE)
    patient_type = models.CharField(choices=type.choices, max_length=10)
    patient_reason_for_visit = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'patient_list'


class PatientStatus(models.Model):
    class Status(TextChoices):
        RECEPTION = "접수", "접수"
        EXAMINATION = "진료", "진료"
        TREATMENT = "치료", "치료"
        PHYSIOTHERAPY = "물리치료", "물리치료"
        PURCHASE = "수납", "수납"

    status_id = models.IntegerField(primary_key=True, auto_created=True)
    patient_id = models.CharField(max_length=40)
    patient_name = models.CharField(max_length=60, null=False)
    status = models.CharField(choices=Status.choices, max_length=10)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'patient_status'

class ClassificationCode(models.Model):
    classification_code = models.CharField(max_length=5, primary_key=True, blank=False, null=False)
    classification_name = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.classification_code + " " + self.classification_name


class MedicalPersonIdentity(models.Model):
    medical_person_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    medical_person_name = models.CharField(max_length=60, blank=False, null=False)
    medical_person_system_id = models.CharField(max_length=20, blank=False, null=False)
    medical_person_gender = models.CharField(max_length=1, blank=False, null=False)
    medical_person_birthday = models.DateField(blank=False, null=False)
    medical_person_phone_number = models.CharField(max_length=15, blank=False, null=False)
    medical_person_main_address = models.TextField(blank=False, null=False)
    medical_person_license = models.TextField(blank=False, null=False)
    classification_code = models.ForeignKey('ClassificationCode', on_delete=models.PROTECT)

    def __str__(self):
        return self.medical_person_name
    class Meta:
        db_table = 'medical_person_identity'


class PatientExamination(models.Model):
    examination_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.ForeignKey(PatientIdentity, on_delete=models.CASCADE)
    medical_person_id = models.ForeignKey(MedicalPersonIdentity, on_delete=models.CASCADE)
    examination_detail = models.TextField(null=False, default='')
    diagnosis_prescription = models.TextField(null=False, default='')
    examination_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.examination_id)

    class Meta:
        db_table = 'patient_examination'


class Image(models.Model):
    image_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    examination_id = models.ForeignKey(PatientExamination, on_delete=models.CASCADE)
    image_title = models.TextField(null=True, default="a.jpg")
    image_url = models.ImageField(null=False, upload_to="uploaded_pictures")
    image_context = models.TextField(null=False, default="a")
    image_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "image"


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
