from django import views
from django.urls import path
from .views import *
urlpatterns = [
    path('test/', download_docx , name='healthcare-test'),
    path('', PatientListView.as_view() , name='healthcare-patient_list'),
    path('<int:pk>/', PatientDetailView.as_view() , name='healthcare-patient_details'),
    path('<int:pk>/update/', PatientUpdateView.as_view() , name='healthcare-patient_update'),  
    path('<int:pk>/delete/', PatientDeleteView.as_view() , name='healthcare-patient_delete'),  
    path('create/', PatientCreateView.as_view() , name='healthcare-patient_create'),
]
