from django.shortcuts import render, redirect, HttpResponse
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import ContactMessage

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('register')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid email or password.')
    
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def level(request):
    return render(request, 'level.html')

def index(request):
    context = {
        "variable" : "Hello, World!"
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        try:
            contact_message = ContactMessage(name=name, email=email, message=message)
            contact_message.save()
            return JsonResponse({'success': True, 'message': 'Message sent successfully and saved to the database!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f"An error occurred: {str(e)}"})

    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

def services(request):
    return HttpResponse("This is services page.")


def faqs(request):
    return render(request, 'faqs.html')

def terms(request):
    return render(request, 'terms.html')

def errorpage(request):
    return render(request, 'errorpage.html')

def subscription(request):
    return render(request, 'subscription.html')

def preferences(request):
    return render(request, 'preferences.html')

def feedback(request):
    return render(request, 'feedback.html')