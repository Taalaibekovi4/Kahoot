from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Class(models.Model):
    school = models.ForeignKey(School, related_name='classes', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    students = models.JSONField()  # Список студентов в классе

    def __str__(self):
        return f"{self.name} - {self.school.name}"

class Level(models.Model):
    title = models.CharField(max_length=255)
    school = models.ForeignKey(School, related_name='levels', on_delete=models.CASCADE)
    participants = models.JSONField()  # Список участников

    def __str__(self):
        return f"{self.title} - {self.school.name}"

class Quiz(models.Model):
    quiz_name = models.CharField(max_length=255)
    level = models.ForeignKey(Level, related_name='quizzes', on_delete=models.CASCADE)
    date = models.DateTimeField()
    winners = models.JSONField()  # Список победителей и их баллы

    def __str__(self):
        return f"{self.quiz_name} - {self.level.title}"

class User(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.URLField()
    schools = models.ManyToManyField(School, related_name='users')

    def __str__(self):
        return self.name
