# Generated by Django 4.2.7 on 2023-12-14 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0006_alter_image_image_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientreception',
            name='patient_id',
            field=models.ForeignKey(db_column='patient_id', on_delete=django.db.models.deletion.CASCADE, to='emr.patientidentity'),
        ),
    ]