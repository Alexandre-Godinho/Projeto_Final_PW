from django.db import models


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    lusofona = models.CharField(max_length=500)
    linkedin = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name}"


class Subject(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    semester = models.IntegerField()
    ects = models.IntegerField()
    lusofona = models.CharField(max_length=500)
    ranking = models.CharField(max_length=5)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.title}"


class Post(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    link = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.title}"
