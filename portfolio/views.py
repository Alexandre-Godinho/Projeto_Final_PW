from django.shortcuts import render
#  hello/views.py
from portfolio.models import Subject, Teacher, Project


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def aboutme_page_view(request):
    return render(request, 'portfolio/aboutme.html')


def projects_page_view(request):
    return render(request, 'portfolio/projects.html')


def graduation_page_view(request):
    context = {'subjects': Subject.objects.all()}
    return render(request, 'portfolio/graduation.html', context)


def index(request):
    pass