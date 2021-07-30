from django.urls import path
from .views import ExpertListView,ExpertCreateView,ExpertDetailView,ExpertUpdateView,ExpertDeleteView

app_name = 'experts'

urlpatterns = [
    path('',ExpertListView.as_view(),name='expert-list'),
    path('<int:pk>/', ExpertDetailView.as_view() , name='expert-detail'),
    path('<int:pk>/update/', ExpertUpdateView.as_view() , name='expert-update'),  
    path('<int:pk>/delete/', ExpertDeleteView.as_view() , name='expert-delete'),  
    path('create/',ExpertCreateView.as_view(),name='expert-create'),

]
