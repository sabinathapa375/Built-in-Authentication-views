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


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('posts')
        else:
            return render(request, 'users/register.html', {'form': form})






