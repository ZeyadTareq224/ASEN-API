# Generated by Django 4.1.8 on 2023-04-26 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Patient",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("status", models.CharField(choices=[("active", "Active"), ("disabled", "Disabled")], max_length=20)),
                ("dob", models.DateField()),
                ("email", models.EmailField(max_length=254)),
                (
                    "gender",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="common.gender"
                    ),
                ),
            ],
        ),
    ]