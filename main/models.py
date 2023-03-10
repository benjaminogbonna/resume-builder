from django.db import models


class Resume(models.Model):
    full_name = models.CharField(max_length=100,)
    title = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=30,)
    phone = models.CharField(max_length=20,)
    address = models.CharField(max_length=50,)
    profile = models.TextField(max_length=1000, default='')

    skills_1 = models.CharField(max_length=20,)
    skills_2 = models.CharField(max_length=20,)
    skills_3 = models.CharField(max_length=20, default='', blank=True)
    skills_4 = models.CharField(max_length=20, default='', blank=True)
    skills_5 = models.CharField(max_length=20, default='', blank=True)
    skills_6 = models.CharField(max_length=20, default='', blank=True,)

    experience_1_title = models.CharField(max_length=50,)
    experience_1_organization = models.CharField(max_length=50, default='')
    experience_1_duration = models.CharField(max_length=20,)
    experience_1_description = models.CharField(max_length=100,)

    experience_2_title = models.CharField(max_length=50, default='', blank=True)
    experience_2_organization = models.CharField(max_length=50, default='', blank=True)
    experience_2_duration = models.CharField(max_length=20, default='', blank=True)
    experience_2_description = models.CharField(max_length=100, default='', blank=True)

    experience_3_title = models.CharField(max_length=50, default='', blank=True)
    experience_3_organization = models.CharField(max_length=50, default='', blank=True)
    experience_3_duration = models.CharField(max_length=15, default='', blank=True)
    experience_3_description = models.CharField(max_length=100, default='', blank=True)

    education_1 = models.CharField(max_length=50,)
    education_1_degree = models.CharField(max_length=40, default='')
    education_1_duration = models.CharField(max_length=20,)

    education_2 = models.CharField(max_length=50, blank=True, default='')
    education_2_degree = models.CharField(max_length=40, blank=True, default='')
    education_2_duration = models.CharField(max_length=20, blank=True, default='')
