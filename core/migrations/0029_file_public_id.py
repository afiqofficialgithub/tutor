# Generated by Django 5.1.1 on 2024-10-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_tempprofile_verification_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='public_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
