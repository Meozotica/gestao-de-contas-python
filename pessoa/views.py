from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("ola Mundo")

# Create your views here.
