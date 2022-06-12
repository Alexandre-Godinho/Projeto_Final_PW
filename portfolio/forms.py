from django import forms
from django.forms import ModelForm
from .models import Teacher, Subject, Project, Post


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ("name", "year", "semester", "ects", "lusofona", "ranking", "teacher")

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome", "max": 50}),
            "year": forms.NumberInput(attrs={"class": "form-control"}),
            "semester": forms.NumberInput(attrs={"class": "form-control"}),
            "ects": forms.NumberInput(attrs={"class": "form-control"}),
            "lusofona": forms.TextInput(attrs={"class": "form-control", "placeholder": "Link da Lusófuna", "max": 500}),
            "ranking": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ranking", "max": 5}),
            "teacher": forms.Select(attrs={"class": "form-control"}),
        }

        labels = {
            "name": "Nome",
            "year": "Ano",
            "semester": "Semestre",
            "ects": "ECTs",
            "lusofona": "Link da Lusófuna",
            "ranking": "Ranking",
        }

        help_texts = {
            "name": "",
            "year": "",
            "semester": "",
            "ects": "",
            "lusofona": "",
            "ranking": "",
        }


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ("title", "description", "image", "subject", "year")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Autor", "max": 50}),
            "description": forms.TextInput(attrs={"class": "form-control", "placeholder": "Descrição", "max": 500}),
            "image": forms.TextInput(attrs={"class": "form-control", "placeholder": "Imagem", "max": 500}),
            "subject": forms.Select(attrs={"class": "form-control"}),
            "year": forms.NumberInput(attrs={"class": "form-control"}),
        }

        labels = {
            "title": "Autor",
            "description": "Descrição",
            "image": "Imagem",
            "year": "Ano",
        }

        help_texts = {
            "title": "",
            "description": "",
            "image": "",
            "year": "",
        }


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("author", "title", "description", "link", "image")

        widgets = {
            "author": forms.TextInput(attrs={"class": "form-control", "placeholder": "Autor", "max": 50}),
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Título", "max": 50}),
            "description": forms.TextInput(attrs={"class": "form-control", "placeholder": "Descrição", "max": 500}),
            "link": forms.TextInput(attrs={"class": "form-control", "placeholder": "Link", "max": 500}),
            "image": forms.TextInput(attrs={"class": "form-control", "placeholder": "Imagem", "max": 500}),
        }

        labels = {
            "author": "Autor",
            "title": "Título",
            "description": "Descrição",
            "link": "Link",
            "image": "Imagem",
        }

        help_texts = {
            "author": "",
            "title": "",
            "description": "",
            "link": "",
            "image": "",
        }
