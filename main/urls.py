from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(),name ='store'),
    path('book/<str:name_barber>', views.BarberTimeList.as_view()),
    path('process_booking', views.process_booking)
]
