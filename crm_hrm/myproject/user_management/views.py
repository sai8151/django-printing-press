# user_management/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile

def user_list(request):
    users = UserProfile.objects.all()
    return render(request, 'user_list.html', {'users': users})

def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        user = User.objects.create_user(username=username, password=password)
        UserProfile.objects.create(user=user, role=role)

        return redirect('user_list')
    return render(request, 'create_user.html')
