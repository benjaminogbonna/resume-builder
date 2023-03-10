from django.shortcuts import render
from .forms import ResumeForm


def index(request):
    return render(request, 'main/index.html')


def create(request):
    form = ResumeForm()
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            full_name = cd['full_name']
            title = cd['title']
            email = cd['email']
            phone = cd['phone']
            address = cd['address']
            profile = cd['profile']

            skills_1 = cd['skills_1']
            skills_2 = cd['skills_2']
            skills_3 = cd['skills_3']
            skills_4 = cd['skills_4']
            skills_5 = cd['skills_5']
            skills_6 = cd['skills_6']

            experience_1_title = cd['experience_1_title']
            experience_1_organization = cd['experience_1_organization']
            experience_1_duration = cd['experience_1_duration']
            experience_1_description = cd['experience_1_description']

            experience_2_title = cd['experience_2_title']
            experience_2_organization = cd['experience_2_organization']
            experience_2_duration = cd['experience_2_duration']
            experience_2_description = cd['experience_2_description']

            experience_3_title = cd['experience_3_title']
            experience_3_organization = cd['experience_3_organization']
            experience_3_duration = cd['experience_3_duration']
            experience_3_description = cd['experience_3_description']

            education_1 = cd['education_1']
            education_1_degree = cd['education_1_degree']
            education_1_duration = cd['education_1_duration']

            education_2 = cd['education_2']
            education_2_degree = cd['education_2_degree']
            education_2_duration = cd['education_2_duration']

            resume_data = {
                'full_name': full_name,
                'title': title,
                'email': email,
                'phone': phone,
                'address': address,
                'profile': profile,

                'skills_1': skills_1,
                'skills_2': skills_2,
                'skills_3': skills_3,
                'skills_4': skills_4,
                'skills_5': skills_5,
                'skills_6': skills_6,

                'experience_1_title': experience_1_title,
                'experience_1_organization': experience_1_organization,
                'experience_1_duration': experience_1_duration,
                'experience_1_description': experience_1_description,

                'experience_2_title': experience_2_title,
                'experience_2_organization': experience_2_organization,
                'experience_2_duration': experience_2_duration,
                'experience_2_description': experience_2_description,

                'experience_3_title': experience_3_title,
                'experience_3_organization': experience_3_organization,
                'experience_3_duration': experience_3_duration,
                'experience_3_description': experience_3_description,

                'education_1': education_1,
                'education_1_degree': education_1_degree,
                'education_1_duration': education_1_duration,

                'education_2': education_2,
                'education_2_degree': education_2_degree,
                'education_2_duration': education_2_duration,
            }

            context = {
                'resume_data': resume_data,
            }

            return render(request, 'main/resume.html', context)

    context = {
        'form': form,
    }
    return render(request, 'main/create.html', context)


def resume(request):
    return render(request, 'main/resume.html')
