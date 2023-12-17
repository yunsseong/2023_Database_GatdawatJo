from django.db import models
import uuid

from django.db.models import TextChoices
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.conf import settings


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 추가 필드 등 사용자 모델 커스터마이징
    name = models.CharField(max_length=100)
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='custom_user_permissions'
    )
class PatientIdentity(models.Model):
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_name = models.CharField(max_length=60, null=False)
    patient_gender = models.CharField(max_length=1, blank=False, null=False)
    patient_birth = models.CharField(max_length=8, blank=False, null=False)
    patient_residence_number = models.CharField(max_length=8, blank=False, null=False)
    patient_phone_number = models.CharField(max_length=15, blank=False, null=False)
    patient_emergency_phone_number = models.CharField(max_length=15)
    patient_address = models.CharField(max_length=100)
    patient_agree_essential_term = models.BooleanField(default=False)
    patient_agree_optional_term = models.BooleanField(default=False)

    class Meta:
        db_table = 'patient_identity'

    def __str__(self):
        return self.patient_name

class Reception(models.Model):
    reception_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey('PatientIdentity', on_delete=models.CASCADE, related_name="patient",  default="")
    visit_reason = models.TextField(blank=False, null=False)
    reception_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reception'

class PatientList(models.Model):
    list_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey('PatientIdentity', on_delete=models.CASCADE)

    class Meta:
        db_table = 'patient_list'

class ClassificationCode(models.Model):
    classification_code = models.CharField(max_length=5, primary_key=True, blank=False, null=False)
    classification_name = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.classification_code + " " + self.classification_name


class MedicalPersonIdentity(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    medical_person_name = models.CharField(max_length=60, blank=False, null=False)
    medical_person_gender = models.CharField(max_length=2, blank=False, null=False)
    medical_person_birthday = models.DateField(blank=False, null=False)
    medical_person_phone_number = models.CharField(max_length=15, blank=False, null=False)
    medical_person_main_address = models.TextField(blank=False, null=False)
    medical_person_license = models.TextField(blank=False, null=False)
    classification_code = models.ForeignKey('ClassificationCode', on_delete=models.PROTECT)

    def __str__(self):
        return self.medical_person_name
    class Meta:
        db_table = 'medical_person_identity'


class Chart(models.Model):
    chart_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(PatientIdentity, on_delete=models.CASCADE, related_name='medical_person_identity')
    medical = models.ForeignKey(MedicalPersonIdentity, on_delete=models.CASCADE)
    diagnosis = models.TextField(null=False, default='')
    inspect = models.ManyToManyField('InspectType', related_name='charts')
    disease = models.ManyToManyField('Disease', related_name='charts')
    doctor_opinion = models.TextField(null=False, default='')
    treatment = models.ManyToManyField('Treatment', related_name='charts')
    medication = models.ManyToManyField('Medication', related_name='charts')
    datetime = models.DateTimeField(auto_now_add=True)
    image_id = models.UUIDField(default=uuid.uuid4, editable=False)
    image_url = models.ImageField(upload_to="uploaded_pictures")

    def __str__(self):
        return str(self.chart_id)

    class Meta:
        db_table = 'chart'

class Disease(models.Model):
    disease_code = models.CharField(max_length=50, unique=True)
    disease_name = models.CharField(max_length=200)
    disease_description = models.TextField()

    def __str__(self):
        return self.disease_name

    class Meta:
        db_table = "disease"

from django.db import models

class Treatment(models.Model):
    treatment_code = models.CharField(primary_key=True, max_length=50, unique=True)
    treatment_name = models.CharField(max_length=200)
    treatment_cost = models.IntegerField()

    def __str__(self):
        return self.treatment_name

    class Meta:
        db_table = "treatment"


class Medication(models.Model):
    medication_code = models.CharField(primary_key=True, max_length=50, unique=True)
    medication_name = models.CharField(max_length=200)
    medication_type = models.CharField(max_length=100)
    medication_description = models.TextField()
    administration_method = models.TextField()
    medication_cost = models.IntegerField()

    def __str__(self):
        return self.medication_name

    class Meta:
        db_table = "medication"

class InspectType(models.Model):
    inspect_type_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inspect_type = models.CharField(max_length=50, verbose_name='검사 종류')
    inspect_cost = models.IntegerField()

    def __str__(self):
        return self.inspect_type

    class Meta:
        db_table = "inspect_type"

class Inspect(models.Model):
    inspect_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.ForeignKey(PatientIdentity, on_delete=models.CASCADE)
    inspect_item = models.ForeignKey(InspectType, on_delete=models.CASCADE)
    inspect_date = models.DateTimeField(auto_now=True)
    inspect_content = models.TextField(verbose_name='검사 내용')

    class Meta:
        db_table = "inspect"

class Image(models.Model):
    image_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chart_id = models.ForeignKey(Chart, on_delete=models.CASCADE)
    image_title = models.TextField(null=True, default="a.jpg")
    image_url = models.ImageField(null=False, upload_to="uploaded_pictures")
    image_context = models.TextField(null=False, default="a")
    image_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "image"

class Inbody(models.Model):
    inbody_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.ForeignKey('PatientIdentity', on_delete=models.PROTECT)
    weight = models.FloatField()
    muscle_mass = models.FloatField()
    body_fat_mass = models.FloatField()
    bmi = models.FloatField()
    percent_body_fat = models.FloatField()
    right_arm = models.FloatField()
    left_arm = models.FloatField()
    trunk = models.FloatField()
    right_leg = models.FloatField()
    left_leg = models.FloatField()
    record_date = models.DateTimeField(auto_now_add=True)
    original_file_location = models.BinaryField()

    class Meta:
        db_table = 'inbody'

class Blood(models.Model):
    blood_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.ForeignKey('PatientIdentity', on_delete=models.PROTECT)
    hemoglobin = models.FloatField(verbose_name='혈색소')
    fasting_blood_sugar = models.FloatField(verbose_name='공복혈당')
    total_cholesterol = models.FloatField(verbose_name='총 콜레스트롤')
    hdl_cholesterol = models.FloatField(verbose_name='HDL-콜레스트롤')
    triglycerides = models.FloatField(verbose_name='중성지방')
    ldl_cholesterol = models.FloatField(verbose_name='LDL-콜레스트롤')
    serum_creatinine = models.FloatField(verbose_name='혈청크레아티닌')
    glomerular_filtration_rate = models.FloatField(verbose_name='신사구체여과율')
    ast = models.FloatField(verbose_name='AST')
    alt = models.FloatField(verbose_name='ALT')
    gamma_gt = models.FloatField(verbose_name='감마지피티')

    class Meta:
        db_table = "blood"


class XRay(models.Model):
    xray_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.ForeignKey(PatientIdentity, on_delete=models.CASCADE)
    medical_person_id = models.ForeignKey(MedicalPersonIdentity, on_delete=models.PROTECT)
    shooting_timestamp = models.DateTimeField()
    original_xray_location = models.BinaryField()

    class Meta:
        db_table = 'xray'
