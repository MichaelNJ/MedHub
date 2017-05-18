from django.shortcuts import render
from django.http import HttpResponse, Http404
from Reception.models import Patient, Aillment
from datetime import datetime
from django.utils import timezone

# Create your views here.
def waiting(request):
    patient_today_name = []
    try:
        p_a = Patient.objects.order_by('-time')

    except Patient.DoesNotExist:
        raise Http404("Got a a error parsing patient data")

    else:
        return render(request, 'doctors/waiting.html', {'pa' : p_a })

def record(request, r_id):

    try:
        all_ids = Patient.objects.all()
        specific_id = Patient.objects.get(pk=r_id)

        p_aill = Aillment.objects.all()

        #p_aill = Aillment.objects.get(pk=r_id)

        fields = {
            'all_ids' : all_ids,
            'p_id' : specific_id,
            'p_ill' : p_aill,
        }

    except Patient.DoesNotExist:
        raise Http404("Got a a error parsing patient data")

    else:
        return render(request, 'doctors/record.html', context=fields)