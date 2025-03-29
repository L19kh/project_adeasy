from django.urls import path
from .views import home
from .views import States
from . import views
from accounts import views
from django.urls import path
from . import views
app_name = 'accounts' 

urlpatterns = [
    path('', views.home, name='home'),
    path('States/', views.States, name='States'),
    path('newspapers/', views.newspapers, name='newspapers'),
    path('kerala/', views.kerala, name='kerala'),
    path('Kerala2/', views.Kerala2, name='Kerala2'),
    path('date/', views.date, name='date'),
    path('date2/', views.date2, name='date2'),
    path('datetoi/', views.datetoi, name='datetoi'),
    path('classeditiontoi/', views.classeditiontoi, name='classeditiontoi'),
    path('editions2/', views.editions2, name='editions2'),
    path('editions/', views.editions, name='editions'),
    path('design/', views.design, name='design'),
    path('designs/', views.designs, name='designs'),
    path('texteditiontoi/', views.texteditiontoi, name='texteditiontoi'),
    path('displaysection/', views.displaysection, name='displaysection'),
    path('classedition/', views.classedition, name='classedition'),
    path('States2/', views.States2, name='States2'),
    path('newspapers2/', views.newspapers2, name='newspapers2'),
    path('fulleditiontoi/', views.fulleditiontoi, name='fulleditiontoi'),
    path('preview/', views.preview, name='preview'),
    path('dispreview/', views.dispreview, name='dispreview'),
    path('previewtoi/', views.previewtoi, name='previewtoi'),
    path('pay/', views.pay, name='pay'),
    path('payment/', views.payment, name='payment'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('dashboard/', views.dashboard, name='dashboard'),

]
