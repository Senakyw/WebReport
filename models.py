from pyexpat import model
from random import choices
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone

class User(models.Model):
    Jobs = [] #liste à remplir
    job = models.CharField(choices = Jobs)

class Projet(models.Model):
    manager = models.ForeignKey(user, on_delete = models.CASCADE, related_name = "manager of")
    label = models.CharField(max_length = 4)
    title = models.CharField(max_length=64)
    description = models.TextField()
    begDate = models.DateTimeField()
    endDate = models.DateTimeField()
    timeBudget = models.IntegerField()
    moneyBudget = models.IntegerField()
    isOpen = models.BooleanField()

class Group(models.Model):
    project = models.ForeignKey(Projet, on_delete = models.CASCADE, related_name ="groups")
    manager = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "manager of")
    label = models.CharField(max_length = 2)
    description = models.TextField()
    begDate = models.DateTimeField()
    endDate = models.DateTimeField()
    timeBudget = models.IntegerField()
    moneyBudget = models.IntegerField()
    isOpen = models.BooleanField()

class Task(models.Model):
    label = models.CharField(max_length = 4)
    group = models.ForeignKey(Group, on_delete =models.CASCADE, related_name = "tasks")
    users = models.ManyToManyField(User,related_name = "tasks")

class Period(models.Model):
    begDate = models.DateTimeField()
    endDate = models.DateTimeField()
    isOpen = models.BooleanField()
    allocTime = models.IntegerField()

class Sample(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT, related_name = "Samples")
    task = models.ForeignKey(Task, on_delete = models.CASCADE, related_name = "Samples")
    period = models.ForeignKey(Period, on_delete = models.CASCADE, related_name ="Samples")
    timeBudget = models.IntegerField()
    moneyBudget = models.IntegerField()