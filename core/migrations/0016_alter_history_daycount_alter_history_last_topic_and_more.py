# Generated by Django 5.1.1 on 2024-10-08 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='daycount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='last_topic',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='payment_status',
            field=models.CharField(blank=True, choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], default='unpaid', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='total_day_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
