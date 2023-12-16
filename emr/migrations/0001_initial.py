# Generated by Django 4.2.7 on 2023-12-14 13:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificationCode',
            fields=[
                ('classification_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('classification_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalPersonIdentity',
            fields=[
                ('medical_person_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('medical_person_name', models.CharField(max_length=60)),
                ('medical_person_system_id', models.CharField(max_length=20)),
                ('medical_person_gender', models.CharField(max_length=2)),
                ('medical_person_birthday', models.DateField()),
                ('medical_person_phone_number', models.CharField(max_length=15)),
                ('medical_person_main_address', models.TextField()),
                ('medical_person_license', models.TextField()),
                ('classification_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emr.classificationcode')),
            ],
            options={
                'db_table': 'medical_person_identity',
            },
        ),
        migrations.CreateModel(
            name='PatientIdentity',
            fields=[
                ('patient_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('patient_name', models.CharField(max_length=60)),
                ('patient_gender', models.CharField(max_length=1)),
                ('patient_birth', models.CharField(max_length=8)),
                ('patient_residence_number', models.CharField(max_length=8)),
                ('patient_phone_number', models.CharField(max_length=15)),
                ('patient_emergency_phone_number', models.CharField(max_length=15)),
                ('patient_address', models.CharField(max_length=100)),
                ('patient_agree_essential_term', models.BooleanField(default=False)),
                ('patient_agree_optional_term', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'patient_identity',
            },
        ),
        migrations.CreateModel(
            name='PatientStatus',
            fields=[
                ('status_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('patient_id', models.CharField(max_length=40)),
                ('patient_name', models.CharField(max_length=60)),
                ('status', models.CharField(choices=[('접수', '접수'), ('진료', '진료'), ('치료', '치료'), ('물리치료', '물리치료'), ('수납', '수납')], max_length=10)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'patient_status',
            },
        ),
        migrations.CreateModel(
            name='PatientXRay',
            fields=[
                ('xray_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('shooting_timestamp', models.DateTimeField()),
                ('original_xray_location', models.BinaryField()),
                ('medical_person_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emr.medicalpersonidentity')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patientidentity')),
            ],
            options={
                'db_table': 'patient_xray',
            },
        ),
        migrations.CreateModel(
            name='PatientReception',
            fields=[
                ('reception_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('visit_reason', models.TextField()),
                ('reception_date', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='emr.patientidentity')),
            ],
            options={
                'db_table': 'patient_reception',
            },
        ),
        migrations.CreateModel(
            name='PatientList',
            fields=[
                ('list_id', models.AutoField(primary_key=True, serialize=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patientidentity')),
            ],
            options={
                'db_table': 'patient_list',
            },
        ),
        migrations.CreateModel(
            name='PatientInbody',
            fields=[
                ('inbody_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('weight', models.FloatField()),
                ('muscle_mass', models.FloatField()),
                ('body_fat_mass', models.FloatField()),
                ('total_body_water', models.FloatField()),
                ('protein', models.FloatField()),
                ('minerals', models.FloatField()),
                ('bmi', models.FloatField()),
                ('percent_body_fat', models.FloatField()),
                ('right_arm', models.FloatField()),
                ('left_arm', models.FloatField()),
                ('trunk', models.FloatField()),
                ('right_leg', models.FloatField()),
                ('left_leg', models.FloatField()),
                ('ecw_ratio', models.FloatField()),
                ('record_date', models.DateField()),
                ('original_file_location', models.BinaryField()),
                ('medical_person_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emr.medicalpersonidentity')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emr.patientidentity')),
            ],
            options={
                'db_table': 'patient_inbody',
            },
        ),
        migrations.CreateModel(
            name='PatientChart',
            fields=[
                ('chart_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('diagnosis', models.TextField(default='')),
                ('prescription', models.TextField(default='')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('image_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('image_title', models.TextField(default=models.UUIDField(default=uuid.uuid4, editable=False))),
                ('image_url', models.ImageField(upload_to='uploaded_pictures')),
                ('medical_person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.medicalpersonidentity')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patientidentity')),
            ],
            options={
                'db_table': 'patient_chart',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image_title', models.TextField(default='a.jpg', null=True)),
                ('image_url', models.ImageField(upload_to='uploaded_pictures')),
                ('image_context', models.TextField(default='a')),
                ('image_date', models.DateTimeField(auto_now_add=True)),
                ('chart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patientchart')),
            ],
            options={
                'db_table': 'image',
            },
        ),
    ]