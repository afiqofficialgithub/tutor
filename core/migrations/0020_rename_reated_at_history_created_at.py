# Generated by Django 5.1.1 on 2024-10-08 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_history_reated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='reated_at',
            new_name='created_at',
        ),
    ]
