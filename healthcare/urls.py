from django import views
from django.urls import path
from .views import *
urlpatterns = [
    path('chart/', search_view , name='healthcare-charts'),
#    path('charts/', ChartData.as_view() , name='charts'),
#    path('search/', SearchPatientFilter.as_view() , name='search'),
    path('searchh/', patient_searchh , name='searchh'),
    path('', PatientListView.as_view() , name='healthcare-patient_list'),
    path('<int:pk>/', PatientDetailView.as_view() , name='healthcare-patient_details'),
    path('<int:pk>/testt/', ExportDocx.as_view() , name='healthcare-testt'),
    path('<int:pk>/update/', PatientUpdateView.as_view() , name='healthcare-patient_update'),  
    path('<int:pk>/delete/', PatientDeleteView.as_view() , name='healthcare-patient_delete'),  
    path('create/', PatientCreateView.as_view() , name='healthcare-patient_create'),
]
