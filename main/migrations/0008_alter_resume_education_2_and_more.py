# Generated by Django 4.0 on 2023-03-10 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_resume_education_1_degree_resume_education_2_degree_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='education_2',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='resume',
            name='education_2_duration',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience_2_description',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience_2_duration',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience_2_organization',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience_2_title',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience_3_description',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience_3_duration',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience_3_organization',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience_3_title',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills_3',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills_4',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills_5',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills_6',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]
