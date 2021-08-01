from django import views
from django.urls import path
from .views import *
urlpatterns = [
    path('test/', download_docx , name='healthcare-test'),
    path('testt/', ExportDocx.as_view() , name='healthcare-testt'),
    path('charts/', ChartData.as_view() , name='charts'),
    path('<int:pk>/chartss/', RetrievePatient.as_view() , name='chartss'),
    path('', PatientListView.as_view() , name='healthcare-patient_list'),
    path('<int:pk>/', PatientDetailView.as_view() , name='healthcare-patient_details'),
    path('<int:pk>/update/', PatientUpdateView.as_view() , name='healthcare-patient_update'),  
    path('<int:pk>/delete/', PatientDeleteView.as_view() , name='healthcare-patient_delete'),  
    path('create/', PatientCreateView.as_view() , name='healthcare-patient_create'),
]
