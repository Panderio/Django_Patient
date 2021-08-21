from . import views
from django.urls import path

app_name ='predict'

urlpatterns = [
    path('', views.predict , name='predict'),
    
    ]