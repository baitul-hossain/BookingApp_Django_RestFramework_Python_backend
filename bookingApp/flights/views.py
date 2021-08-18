from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from django.contrib.auth.models import User


def index(request):
    return HttpResponse("<h1>Hello world!</h1>")

#class UserViewSet(viewsets.ModelViewSet):


