# Generated by Django 5.1.1 on 2024-10-12 21:45

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_userprofile_verification_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempprofile',
            name='verification_token',
            field=models.CharField(blank=True, default=uuid.uuid4, editable=False, null=True),
        ),
    ]