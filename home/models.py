from django.db import models


# Create your models here.
class Question(models.Model):
    query = models.CharField(max_length=255)
    index = models.IntegerField(default=0)


class Answer(models.Model):
    query = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, blank=True)
    answer = models.CharField(max_length=500, null=True)


class User(models.Model):
    name = models.CharField(max_length=255)
    answer = models.ManyToManyField(Answer)
    create_date = models.DateField(auto_now_add=True)
    step = models.IntegerField(default=-1)