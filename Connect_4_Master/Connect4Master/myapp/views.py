# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomLoginForm

def register_view(request):
    """Handle user registration."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Automatically log in the user after registration
            messages.success(request, 'Registration successful! You are now logged in.')
            return redirect('login_view')  # Redirect to the login page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration.html', {'form': form})

def login_view(request):
    """Handle user login."""
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                auth_login(request, user)
                # messages.success(request, 'Login successful!')
                return render(request,'index.html')  # Redirect to index page or wherever appropriate
        else:
            # Add an error message if form is not valid
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})


def index_view(request):
    return render(request,'index.html')

def playwithfriend_view(request):
    return render(request, 'playwithfriend.html')

def playwithcomputer_view(request):
    return render(request, 'playwithcomputer.html')