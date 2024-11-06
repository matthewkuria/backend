from django.urls import path
from .views import  LoginView, RegisterView, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user-register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('user-profile/', UserProfileView.as_view(), name='user-profile'),
]
