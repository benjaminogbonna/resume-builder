# Generated by Django 4.0 on 2023-03-10 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_resume_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='profile',
            field=models.TextField(default='', max_length=200),
        ),
    ]