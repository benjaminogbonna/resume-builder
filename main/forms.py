from django import forms
from .models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name*', 'class': 'form-control form-control-lg'}),
            'title': forms.TextInput(attrs={'placeholder': 'Title*', 'class': 'form-control form-control-lg'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email*', 'class': 'form-control form-control-lg'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone (+2348129944424)*',
                                            'class': 'form-control form-control-lg'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address*', 'class': 'form-control form-control-lg'}),
            'profile': forms.Textarea(attrs={'placeholder': 'Profile: a little about you*',
                                             'class': 'form-control form-control-lg', 'rows': 4}),
            'skills_1': forms.TextInput(attrs={'placeholder': 'skill 1*', 'class': 'form-control form-control-lg'}),
            'skills_2': forms.TextInput(attrs={'placeholder': 'skill 2*', 'class': 'form-control form-control-lg'}),
            'skills_3': forms.TextInput(attrs={'placeholder': 'skill 3', 'class': 'form-control form-control-lg'}),
            'skills_4': forms.TextInput(attrs={'placeholder': 'skill 4', 'class': 'form-control form-control-lg'}),
            'skills_5': forms.TextInput(attrs={'placeholder': 'skill 5', 'class': 'form-control form-control-lg'}),
            'skills_6': forms.TextInput(attrs={'placeholder': 'skill 6', 'class': 'form-control form-control-lg'}),

            'experience_1_title': forms.TextInput(attrs={'placeholder': 'Experience one*',
                                                         'class': 'form-control form-control-lg'}),
            'experience_1_organization': forms.TextInput(attrs={'placeholder': 'Organization one*',
                                                         'class': 'form-control form-control-lg'}),
            'experience_1_duration': forms.TextInput(attrs={'placeholder': 'Duration: 2021-2023*',
                                                            'class': 'form-control form-control-lg'}),
            'experience_1_description': forms.TextInput(attrs={'placeholder': 'Responsibilities*',
                                                               'class': 'form-control form-control-lg'}),

            'experience_2_title': forms.TextInput(attrs={'placeholder': 'Experience two',
                                                         'class': 'form-control form-control-lg'}),
            'experience_2_organization': forms.TextInput(attrs={'placeholder': 'Organization two',
                                                         'class': 'form-control form-control-lg'}),
            'experience_2_duration': forms.TextInput(attrs={'placeholder': 'Duration: 2021-2023',
                                                            'class': 'form-control form-control-lg'}),
            'experience_2_description': forms.TextInput(attrs={'placeholder': 'Responsibilities',
                                                               'class': 'form-control form-control-lg'}),

            'experience_3_title': forms.TextInput(attrs={'placeholder': 'Experience three',
                                                         'class': 'form-control form-control-lg'}),
            'experience_3_organization': forms.TextInput(attrs={'placeholder': 'Organization three',
                                                         'class': 'form-control form-control-lg'}),
            'experience_3_duration': forms.TextInput(attrs={'placeholder': 'Duration: 2021-2023',
                                                            'class': 'form-control form-control-lg'}),
            'experience_3_description': forms.TextInput(attrs={'placeholder': 'Responsibilities',
                                                               'class': 'form-control form-control-lg'}),

            'education_1': forms.TextInput(attrs={'placeholder': 'Education one*',
                                                  'class': 'form-control form-control-lg'}),
            'education_1_degree': forms.TextInput(attrs={'placeholder': 'Education degree*',
                                                         'class': 'form-control form-control-lg'}),
            'education_1_duration': forms.TextInput(attrs={'placeholder': 'Duration: 2021-2023*',
                                                           'class': 'form-control form-control-lg'}),

            'education_2': forms.TextInput(attrs={'placeholder': 'Education two',
                                                  'class': 'form-control form-control-lg'}),
            'education_2_degree': forms.TextInput(attrs={'placeholder': 'Education degree',
                                                  'class': 'form-control form-control-lg'}),
            'education_2_duration': forms.TextInput(attrs={'placeholder': 'Duration: 2021-2023',
                                                           'class': 'form-control form-control-lg'}),
        }
