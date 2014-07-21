from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Pantalla de Inicio")

def home2(request):
    return HttpResponse("Pantalla de Inicio Home2")
