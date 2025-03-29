"""
URL configuration for adeasy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from accounts.views import home  # Import the home view
from accounts import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Map the root URL to the home view
    path('accounts/', include('accounts.urls')),  # Include the app's URLs
    path('States/', views.States, name='States'),
    path('kerala/', views.kerala, name='kerala'),
    path('date/', views.date, name='date'),
    path('date2/', views.date2, name='date2'),
    path('datetoi/', views.datetoi, name='datetoi'),
    path('classeditiontoi/', views.classeditiontoi, name='classeditiontoi'),
    path('editions2/', views.editions2, name='editions2'),
    path('design/', views.design, name='design'),
    path('designs/', views.designs, name='designs'),
    path('classedition/', views.classedition, name='classedition'),
    path('editions/', views.editions, name='editions'),
    path('displaysection/', views.displaysection, name='displaysection'),
    path('States2/', views.States2, name='States2'),
    path('Kerala2/', views.Kerala2, name='Kerala2'),
    path('newspapers2/', views.newspapers2, name='newspapers2'),
    path('fulleditiontoi/', views.fulleditiontoi, name='fulleditiontoi'),
    path('preview/', views.preview, name='preview'),
    path('dispreview/', views.dispreview, name='dispreview'),
    path('texteditiontoi/', views.texteditiontoi, name='texteditiontoi'),
    path('previewtoi/', views.previewtoi, name='previewtoi'),
    path('pay/', views.pay, name='pay'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('payment/', views.payment, name='payment'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

