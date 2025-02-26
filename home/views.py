from django.shortcuts import render, redirect, HttpResponse
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import ContactMessage
import logging
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login as auth_login


logging.basicConfig(level=logging.ERROR)

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                email = form.cleaned_data.get('email')
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'A user with this email already exists.')
                else:
                    form.save()
                    messages.success(request, 'Registration successful! Please login.')
                    return redirect('login')
            except IntegrityError:
                messages.error(request, 'An error occurred. Please try again.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid password. Please try again.')
        except User.DoesNotExist:
            messages.error(request, 'Email not found. Please register first.')
            return redirect('register')

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
            logging.error("An error occurred while saving the contact message", exc_info=True)
            return JsonResponse({'success': False, 'message': "An internal error has occurred. Please try again later."})

    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

def services(request):
    return HttpResponse("This is services page.")


def faqs(request):
    return render(request, 'faqs.html')

def leaderboard(request):
    return render(request, 'leaderboard.html')

def p1s1(request):
    return render(request, 'p1s1.html')

def p1s2(request):
    return render(request, 'p1s2.html')

def p1s3(request):
    return render(request, 'p1s3.html')

def p1s4(request):
    return render(request, 'p1s4.html')

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