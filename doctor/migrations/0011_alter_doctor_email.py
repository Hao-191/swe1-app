# Generated by Django 4.2.4 on 2023-10-22 21:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doctor", "0010_remove_doctor_first_name_remove_doctor_last_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="email",
            field=models.EmailField(
                default="example@example.com", max_length=254, unique=True
            ),
        ),
    ]
