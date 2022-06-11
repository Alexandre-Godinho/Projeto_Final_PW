from django.contrib import admin
from .models import Teacher, Subject, Project, Post


# Register your models here.
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Project)
admin.site.register(Post)
