from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Assalomu alaykum")

def index2(request):
    return HttpResponse("Vaalykum assalom")
