from django.shortcuts import render

# Create your views here.
from django.db import models

class Usuario(models.Model):
    login = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
