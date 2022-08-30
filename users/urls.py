from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/<str:pk>/', views.UserProfileView.as_view(), name='profile'),
    path('profile/<str:pk>/edit',
         views.UserUpdateView.as_view(), name='profile_edit'),
]
