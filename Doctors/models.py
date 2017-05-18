from __future__ import unicode_literals

from django.db import models


class Doctor(models.Model):
    doctor_fname = models.CharField(max_length=30)
    doctor_mname = models.CharField(max_length=30)
    doctor_sname = models.CharField(max_length=30)

    doctor_age = models.IntegerField()
    doctor_id = models.IntegerField()

    def __str__(self):
        return "%s %s" %(self.doctor_fname, self.doctor_mname)

#class Aillment(models.Model):

