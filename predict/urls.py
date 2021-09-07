from .views import predict
from django.urls import path

app_name ='predict'

urlpatterns = [
    path('', predict , name='predict'),
    
    ]