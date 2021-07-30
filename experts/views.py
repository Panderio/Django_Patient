from django.shortcuts import redirect, render, reverse 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from healthcare.models import Expert
from .forms import ExpertModelForm
from .mixins import ExpertandLoginRequiredMixin

# Create your views here.



#Class Based Views


#2
class ExpertListView(ExpertandLoginRequiredMixin, generic.ListView):
    template_name="experts/expert_list.html"
    def get_queryset(self):
        doct = self.request.user.userprofile
        return Expert.objects.filter(docteur=doct)

class ExpertCreateView(ExpertandLoginRequiredMixin,generic.CreateView):
    template_name="experts/expert_create.html"
    form_class=ExpertModelForm
    def get_success_url(self):
        return reverse("experts:expert-list")
    def form_valid(self, form):
        expert = form.save(commit=False)
        expert.docteur = self.request.user.userprofile
        expert.save()
        return super(ExpertCreateView,self).form_valid(form)

class ExpertDetailView(ExpertandLoginRequiredMixin, generic.DetailView):
    template_name="experts/expert_detail.html"
    context_object_name="expert"
    def get_queryset(self):
        doct = self.request.user.userprofile
        return Expert.objects.filter(docteur=doct)

class ExpertUpdateView(ExpertandLoginRequiredMixin,generic.UpdateView):
    template_name="experts/expert_update.html"
    form_class=ExpertModelForm

    def get_success_url(self):
        return reverse("experts:expert-list")
    
    def get_queryset(self):
        return Expert.objects.all()


class ExpertDeleteView(ExpertandLoginRequiredMixin, generic.DeleteView):
    template_name="experts/expert_delete.html"
    context_object_name="expert"
    def get_success_url(self):
        return reverse("experts:expert-list")
    def get_queryset(self):
        doct = self.request.user.userprofile
        return Expert.objects.filter(docteur=doct)
    

