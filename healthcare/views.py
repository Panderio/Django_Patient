from django.core.mail import send_mail
from django.shortcuts import redirect, render, reverse 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Patient
from .forms import PatientForm , PatientModelForm , CustomUserCreation
# Create your views here.



#Class Based Views

#USER
class SignupView(generic.CreateView):
    template_name="registration/signup.html"
    form_class=CustomUserCreation

    def get_success_url(self):
        return reverse("login")


#1
class LandingPageView(generic.TemplateView):
    template_name="landing.html"


#2
class PatientListView(LoginRequiredMixin, generic.ListView):
    template_name="healthcare/patient_list.html"
    queryset=Patient.objects.all()
    context_object_name="patients"


#3
class PatientDetailView(LoginRequiredMixin, generic.DetailView):
    template_name="healthcare/patient_details.html"
    queryset=Patient.objects.all()
    context_object_name="patient"

#4
class PatientCreateView(LoginRequiredMixin, generic.CreateView):
    template_name="healthcare/patient_create.html"
    form_class=PatientModelForm

    def get_success_url(self):
        return reverse("healthcare:healthcare-patient_list")
    def form_valid(self,form):
        #TODO SENT EMAIL 
        send_mail(
            subject="A Patient Has Been Added", 
            message="check the List Patients for the new patient",
            from_email="test@test.com",
            recipient_list=["test2@test.com"] 
        )
        return super(PatientCreateView,self).form_valid(form)

#5
class PatientUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name="healthcare/patient_update.html"
    queryset=Patient.objects.all()
    form_class=PatientModelForm
    def get_success_url(self):
        return reverse("healthcare:healthcare-patient_list")


#6
class PatientDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name="healthcare/patient_delete.html"
    queryset=Patient.objects.all()
    context_object_name="patient"
    def get_success_url(self):
        return reverse("healthcare:healthcare-patient_list")

# Function Based Views
#1
def landing_page(request):
    return render(request, 'healthcare/landing.html')

#2
def patient_list(request):
    patients = Patient.objects.all()
    context = {
        "patients":patients
    }
    return render(request, 'healthcare/patient_list.html', context)

#3
def patient_details(request,pk):
    patient = Patient.objects.get(id=pk)
    context = {
        "patient":patient
    }
    return render(request, 'healthcare/patient_details.html',context)

#4
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


#5
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



def patient_delete(request,pk):
    patient = Patient.objects.get(id=pk)
    patient.delete()
    return redirect("/")



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