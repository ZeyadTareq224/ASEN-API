# Generated by Django 4.1.8 on 2023-04-28 17:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patients", "0003_alter_patient_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="patient",
            name="email",
        ),
        migrations.AlterField(
            model_name="patient",
            name="dob",
            field=models.DateField(blank=True, null=True),
        ),
    ]
