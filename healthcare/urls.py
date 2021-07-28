from django.urls import path
from . import views
urlpatterns = [
    path('', views.patient_list , name='healthcare-patient_list'),
    path('<int:pk>/', views.patient_details , name='healthcare-patient_details'),
    path('<int:pk>/update/', views.patient_update , name='healthcare-patient_update'),  
    path('<int:pk>/delete/', views.patient_delete , name='healthcare-patient_delete'),  
    path('create/', views.patient_create , name='healthcare-patient_create'),
]
