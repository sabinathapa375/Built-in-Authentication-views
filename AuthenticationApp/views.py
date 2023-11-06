from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'registration/Dashboard.html',{'section':'dashboard'})


 






