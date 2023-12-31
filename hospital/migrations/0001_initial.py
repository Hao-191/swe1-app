# Generated by Django 4.2.4 on 2023-10-10 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("user", "0001_initial"),
        ("doctor", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hospital",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("facility_type", models.CharField(max_length=100)),
                (
                    "borough",
                    models.CharField(
                        choices=[
                            ("BKN", "Brooklyn"),
                            ("MHT", "Manhattan"),
                            ("QNS", "Queens"),
                            ("BRX", "Bronx"),
                            ("SND", "Staten Island"),
                        ],
                        max_length=50,
                    ),
                ),
                ("phone", models.CharField(max_length=15)),
                ("location", models.CharField(max_length=200)),
                ("postal_code", models.IntegerField()),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("nta", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="HospitalAppointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("reason", models.CharField(max_length=300)),
                ("accebility", models.CharField(blank=True, max_length=1000)),
                ("start_time", models.DateTimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("REQ", "Requested"),
                            ("CNF", "Confirmed"),
                            ("CCL", "Cancelled"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "hospital",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospital.hospital",
                    ),
                ),
                (
                    "preferred_doctor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="preferred_doctor",
                        to="doctor.doctor",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.user"
                    ),
                ),
            ],
        ),
    ]
