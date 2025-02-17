from django.shortcuts import render, redirect, HttpResponse
from .forms import UserForm
from django.contrib import messages

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


def index(request):
    context = {
        "variable" : "Hello, World!"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return HttpResponse("This is services page.")

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

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