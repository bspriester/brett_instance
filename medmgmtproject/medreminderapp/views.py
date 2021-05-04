from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the medreminderapp index.")


def home_handler(request):
    context = {
        'name': 'Julie'
    }
    return render(request, 'home.html', context)


def medications_handler(request):
    return render(request, 'medications.html')


def reminders_handler(request):
    return render(request, 'reminders.html')


def history_handler(request):
    return render(request, 'history.html')


def login_handler(request):
    return render(request, 'login.html')

def signup_handler(request):
    return render(request, 'signup.html')
