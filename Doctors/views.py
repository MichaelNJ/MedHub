from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'doctors/record.html')

def waiting(request):
    return render(request, 'doctors/waiting.html')