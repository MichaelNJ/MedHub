from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Patient, Aillment
from django.views.generic import UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy


# Create your views here.

def index(request):
    return render(request, 'reception/searcher.html')

def add(request):
    return render(request, 'reception/add.html')

def refer(request, n_id):
    return HttpResponse("You requested patient ID %s" % n_id)

def viewall(request):
    try:
        p_a = Patient.objects.order_by('-time')

        context = {'pa' : p_a}

    except Patient.DoesNotExist:
        return Http404("Got a a error parsing patient data")

    finally:    
        return render(request, 'reception/viewall.html', {'pa' : p_a })

def history(request, h_id):
    p_h = Patient.objects.get(pk=h_id)
    return render(request, 'reception/history.html', {'ph' : p_h})
