from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient
from django.views.generic import UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy


# Create your views here.

def index(request):
    return render(request, 'reception/searcher.html')

def add(request):
    return render(request, 'reception/add.html')

def refer(request, n_id):
    return HttpResponse("You requested patient ID %s" % n_id)

#def savenew(request):
#    model = Patient
#    fields = ["patient_fname", "patient_mname", "patient_sname", "patient_id", "", ""]
