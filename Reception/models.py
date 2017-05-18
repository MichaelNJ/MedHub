from __future__ import unicode_literals

from django.db import models


YEAR_CHOICES = (
    ('Y4S1', 'Year 4 Semester 1'),
    ('Y4S2', 'Year 4 Semester 2'),
    ('Y3S1', 'Year 3 Semester 1'),
    ('Y3S2', 'Year 3 Semester 2'),
    ('Y2S1', 'Year 3 Semester 1'),
    ('Y2S2', 'Year 2 Semester 1'),
    ('Y1S1', 'Year 1 Semester 1'),
    ('Y1S2', 'Year 1 Semester 2')
)


class Patient(models.Model):
    patient_fname = models.CharField(max_length=30)
    patient_mname = models.CharField(max_length=30)
    patient_sname = models.CharField(max_length=30)
    patient_id = models.IntegerField()
    patient_age = models.DateField()
    patient_email = models.EmailField()

    time = models.DateTimeField()

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    current_year = models.CharField(max_length=4, choices=YEAR_CHOICES)
    patient_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return "%s %s" %(self.patient_fname, self.patient_mname)


class Aillment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    height = models.IntegerField()
    weight = models.IntegerField()
    notes = models.CharField(max_length=1000)
    prescription = models.CharField(max_length=500)
    date = models.DateTimeField(['%Y-%m-%d %H:%M'])

    def __str__(self):
        return "Patient %s with the ailling from %s ..." %(self.patient, self.notes[:20])




