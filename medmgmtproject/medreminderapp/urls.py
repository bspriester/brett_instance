from django.urls import path

from .views import home_handler, medications_handler, reminders_handler, history_handler, login_handler

urlpatterns = [
    path('', home_handler, name='Home'),
    path('medications', medications_handler, name='Medications'),
    path('reminders', reminders_handler, name='Reminders'),
    path('history', history_handler, name='History'),
    path('accounts/login', login_handler, name='Login'),
]
