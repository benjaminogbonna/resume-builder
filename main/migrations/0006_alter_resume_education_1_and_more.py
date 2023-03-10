# Generated by Django 4.0 on 2023-03-10 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_resume_education_2_resume_education_2_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='education_1',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='resume',
            name='education_1_duration',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='resume',
            name='education_2',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='education_2_duration',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience_1_description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience_1_duration',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience_1_title',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience_2_description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience_2_duration',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience_2_title',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience_3_description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience_3_title',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]