# Generated by Django 5.1.1 on 2024-10-12 21:30

import cloudinary.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_alter_hwfiles_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('mobile_no', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('picture', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='user')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], max_length=5)),
                ('verification_token', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True)),
                ('token_created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='user'),
        ),
    ]