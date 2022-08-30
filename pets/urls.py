from django.urls import path
from . import views

urlpatterns = [
    path('', views.Pets.as_view(), name='pets'),
    path('<int:pk>/', views.PetDetailView.as_view(), name='pet_detail'),
    path('<int:pk>/edit/', views.PetUpdateView.as_view(), name='pet_edit'),
    path('<int:pk>/delete/', views.PetDeleteView.as_view(), name='pet_delete'),
    path('new/', views.PetCreateView.as_view(), name='pet_new'),
]
