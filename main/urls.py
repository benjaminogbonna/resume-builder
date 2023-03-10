from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('resume/', views.resume, name='resume'),
]
