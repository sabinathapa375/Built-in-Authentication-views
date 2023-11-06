from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from unicodedata import name
from .views import sign_up

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('register/', views.sign_up, name='register'),
    
    
    #For the password change
    path('password_change', auth_views.PasswordChangeView.as_view(), name = "password_change"),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    
    
    #Password Reset 
    path('password_reset', auth_views.PasswordResetView.as_view(), name = 'password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = "password_reset_confirm")
]
