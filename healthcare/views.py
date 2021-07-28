from django.shortcuts import redirect, render
from .models import Patient
from .forms import PatientForm , PatientModelForm
# Create your views here.


def patient_list(request):
    patients = Patient.objects.all()
    context = {
        "patients":patients
    }
    return render(request, 'healthcare/patient_list.html', context)

def patient_details(request,pk):
    patient = Patient.objects.get(id=pk)
    context = {
        "patient":patient
    }
    return render(request, 'healthcare/patient_details.html',context)

def patient_update(request,pk):
    patient = Patient.objects.get(id=pk)
    form=PatientModelForm(instance=patient)
    if request.method == "POST":
        form=PatientModelForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form":form,
        "patient":patient
    }
    return render(request, 'healthcare/patient_update.html',context)

def patient_create(request):
    form=PatientModelForm()
    if request.method == "POST":
        form=PatientModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form":form
    }
    return render(request, 'healthcare/patient_create.html',context)

def patient_delete(request,pk):
    patient = Patient.objects.get(id=pk)
    patient.delete()
    return redirect("/")

def landing_page(request):
    return render(request, 'healthcare/landing.html')


"""
OLD METHOD

def patient_create(request):
    form=PatientForm()
    if request.method == "POST":
        form=PatientForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            civil = form.cleaned_data["civil"]
            matricule = form.cleaned_data["matricule"]
            cin = form.cleaned_data["cin"]
            age = form.cleaned_data["age"]
            Patient.objects.create(
                first_name=first_name,
                last_name=last_name,
                civil=civil,
                matricule=matricule,
                cin=cin,
                age=age
            )
            return redirect("/")
    context = {
        "form":form
    }
    return render(request, 'healthcare/patient_create.html',context)
"""