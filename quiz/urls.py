from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.welcome,name="welcome"), #Welcome page will be shown only once since sessions are created
    path('quiz/', views.quiz,name="quiz"), #This endpoint consists of Quiz Question
    path('dashboard/', views.dashboard,name="dashboard"), #This endpoint consists of User Performance
    path('submission/', views.submission,name="submission"), #This endpoint receives a POST request and updates the user performance

]