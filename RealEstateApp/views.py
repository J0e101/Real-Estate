
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from RealEstateApp.models import *


# Create your views here.
def home(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # Check if the user exists
        if user is not None:
            # login(request, user)
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('/home')
        else:
            messages.error(request, "Invalid login credentials")

    return render(request, 'login.html')

def register(request):
    """ Show the registration form """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check the password
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Display a message
                messages.success(request, "Account created successfully")
                return redirect('/login')
            except:
                # Display a message if the above fails
                messages.error(request, "Username already exist")
        else:
            # Display a message saying passwords don't match
            messages.error(request, "Passwords do not match")

    return render(request, 'register.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def agents(request):
    return render(request, 'agents.html')

def properties(request):
    return render(request, 'properties.html')

def services(request):
    return render(request, 'services.html')

def propingles(request):
    return render(request, 'property-single.html')

def servetails(request):
    return render(request, 'service-details.html')

def showcontacts(request):
    all = Contact.objects.all()
    return render(request, 'showcontacts.html', {'contacts': all})



