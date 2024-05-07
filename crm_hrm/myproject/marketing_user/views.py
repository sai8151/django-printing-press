# marketing_user/views.py
from django.shortcuts import render, redirect
from .models import Client
from django.contrib.auth.models import User  # Import the User model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse

@login_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

@login_required
def add_client(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        # Check if a client with the same user ID already exists
        existing_client = Client.objects.filter(user_id=user_id).exists()
        if existing_client:
            # If a client with the same user ID exists, handle the case accordingly
            # For example, you can display a message to the user or redirect to another page
            return render(request, 'client_exists.html')  # Create a template for this

        # Create a new User
        user = User.objects.create_user(username=user_id, password=password)

        # Add the user to the clients_group
        clients_group = Group.objects.get(name='clients_group')  # Replace 'clients_group' with your actual group name
        user.groups.add(clients_group)

        # Create a new Client linked to the User
        client = Client.objects.create(name=name, user=user, password=password)

        # Redirect to client list after successful creation
        return redirect('client_list')

    return render(request, 'add_client.html')

@login_required
def profile(request):
    user = request.user
    marketing_group = Group.objects.get(name='marketing_group')  # Replace 'marketing_group' with your actual group name
    clients_group = Group.objects.get(name='clients_group')  # Replace 'clients_group' with your actual group name
    
    if marketing_group in user.groups.all():
        # User belongs to the marketing group
        clients = Client.objects.all()
        return render(request, 'client_list.html', {'clients': clients})

    elif clients_group in user.groups.all():
        # User belongs to the clients group
        pass
    
    # If the user doesn't belong to any group, or belongs to a group not handled above
    return HttpResponse("This is the default profile view")

@login_required
def upload_csv(request):
    # Your view logic goes here
    return render(request, 'upload_csv.html')