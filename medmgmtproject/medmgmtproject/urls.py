"""medmgmtproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # Changed by Brett.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medreminderapp.urls')),
    path('accounts/', include('accounts.urls')), # Added by Brett for signup feature.
    path('accounts/', include('django.contrib.auth.urls')),
    #Didn't include the following from the tutorial I'm using since I don't want to mess up the current home page setup: 
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
