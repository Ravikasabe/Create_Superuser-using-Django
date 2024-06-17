# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SuperuserCreationForm

def create_superuser(request):
    if request.method == 'POST':
        form = SuperuserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Superuser created successfully.')
            return redirect('create_superuser')
    else:
        form = SuperuserCreationForm()
    return render(request, 'accounts/create_superuser.html', {'form': form})
