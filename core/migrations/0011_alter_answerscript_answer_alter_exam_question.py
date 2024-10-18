# Generated by Django 5.1.1 on 2024-10-07 19:42

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_folder_unique_together_folder_user_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerscript',
            name='answer',
            field=models.FileField(upload_to=core.models.answer_upload_path),
        ),
        migrations.AlterField(
            model_name='exam',
            name='question',
            field=models.FileField(upload_to=core.models.question_upload_path),
        ),
    ]
