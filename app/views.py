"""
Definition of views.
"""

from django import forms
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.template import RequestContext
from datetime import datetime
from .models import *

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    doctors=Doctor.objects.all()
    patients=Patient.objects.all()
    
    if(request.method=='POST'):
        doc=request.POST.get("doctor")
        pat=request.POST.get("patient")
        appointment=Appointment(patient=Patient.objects.get(pk=pat),doctor=Doctor.objects.get(pk=doc),datetime=request.POST.get("appDate"))
        appointment.save()
    appointments = Appointment.objects.select_related('doctor','patient') #inner join of appointmnets,patients,doctors
    print(str(appointments.query))
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'doctors':doctors,
            'patients':patients,
			'appointments':appointments,
        }
    )

def registerDoctor(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    if(request.method=='POST'):
        form=DoctorForm(request.POST)
        if (form.is_valid()):
            doctor=Doctor(name=form.cleaned_data['doc_name'],speciality=form.cleaned_data['doc_spec'])
            doctor.save()
    else:
        form=DoctorForm()
    return render(
        request,
        'app/regDoc.html',
        {
            'title':'Register',
            'message':'Register a new doctor',
            'year':datetime.now().year,
            'form':form
        }
    )

def registerPatient(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    form=PatientForm()

    return render(
        request,
        'app/regPat.html',
        {
            'title':'Register',
            'message':'Register a new patient',
            'year':datetime.now().year,
            'form':form,
        }
    )

class DoctorForm(forms.Form):
    doc_name=forms.CharField(label='Doctor name', max_length=200)
    doc_spec=forms.CharField(label='Speciality',max_length=200)

class PatientForm(forms.Form):
    pat_name=forms.CharField(label='Patient name', max_length=200)
    pat_DOB=forms.DateField(label='DOB')
