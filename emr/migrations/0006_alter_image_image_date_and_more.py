# Generated by Django 5.0 on 2023-12-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("emr", "0005_remove_medicalpersonidentity_medical_person_detail_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="image_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="patientexamination",
            name="examination_datetime",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]