from django.shortcuts import render,HttpResponseRedirect

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'accounts/home.html')

from django.shortcuts import render, redirect
from django.contrib.auth import login

def States(request):
    return render(request, 'accounts/States.html')

def newspapers(request):
    return render(request, 'accounts/newspapers.html')

def kerala(request):
    return render(request, 'accounts/kerala.html')

def date(request):
    return render(request, 'accounts/date.html')

def date2(request):
    return render(request, 'accounts/date2.html')

def datetoi(request):
    return render(request, 'accounts/datetoi.html')

def classeditiontoi(request):
    return render(request, 'accounts/classeditiontoi.html')

def editions2(request):
    return render(request, 'accounts/editions2.html')

def editions(request):
    return render(request, 'accounts/editions.html')

def design(request):
    return render(request, 'accounts/design.html')

def designs(request):
    return render(request, 'accounts/designs.html')

def displaysection(request):
    return render(request, 'accounts/displaysection.html')

def classedition(request):
    return render(request, 'accounts/classedition.html')

def States2(request):
    return render(request, 'accounts/States2.html')

def Kerala2(request):
    return render(request, 'accounts/Kerala2.html')

def newspapers2(request):
    return render(request, 'accounts/newspapers2.html')

def fulleditiontoi(request):
    return render(request, 'accounts/fulleditiontoi.html')

def preview(request):
    return render(request, 'accounts/preview.html')

def dispreview(request):
    return render(request, 'accounts/dispreview.html')

def previewtoi(request):
    return render(request, 'accounts/previewtoi.html')

def texteditiontoi(request):
    return render(request, 'accounts/texteditiontoi.html')

def pay(request):
    return render(request, 'accounts/pay.html')

def payment(request):
    return render(request, 'accounts/payment.html')

def confirmation(request):
    return render(request, 'accounts/confirmation.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
