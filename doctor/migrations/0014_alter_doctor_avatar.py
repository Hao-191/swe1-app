# Generated by Django 4.2.4 on 2023-11-07 19:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doctor", "0013_doctor_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="avatar",
            field=models.ImageField(
                blank=True,
                default="avatars/default-avatar.png",
                null=True,
                upload_to="avatars/",
            ),
        ),
    ]
