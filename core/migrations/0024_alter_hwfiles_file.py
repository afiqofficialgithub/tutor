# Generated by Django 5.1.1 on 2024-10-11 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_alter_answerscript_answer_alter_exam_question_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hwfiles',
            name='file',
            field=models.URLField(max_length=255),
        ),
    ]