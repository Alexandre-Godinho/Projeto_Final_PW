import datetime

from django.shortcuts import render, redirect
from portfolio.forms import SubjectForm, ProjectForm, PostForm
from portfolio.models import Subject, Project, Post


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def aboutme_page_view(request):
    return render(request, 'portfolio/aboutme.html')


def projects_page_view(request):
    context = {'projects': Project.objects.all()}
    return render(request, 'portfolio/projects.html', context)


def graduation_page_view(request):
    context = {'subjects': Subject.objects.all()}
    return render(request, 'portfolio/graduation.html', context)


def blog_page_view(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'portfolio/blog.html', context)


def add_subject_view(request):
    form = SubjectForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("portfolio:home")
    context = {'form': form}
    return render(request, 'portfolio/add_subject.html', context)


def remove_subject_view(request):
    return


def add_project_view(request):
    form = ProjectForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("portfolio:home")
    context = {'form': form}
    return render(request, 'portfolio/add_project.html', context)


def remove_project_view(request):
    return


def add_post_view(request):
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("portfolio:blog")
    context = {'form': form}
    return render(request, 'portfolio/add_post.html', context)


def remove_post_view(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect("portfolio:blog")


def index(request):
    pass