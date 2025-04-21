from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("admin/", admin.site.urls),
    path('api/get_quiz/', views.get_quiz, name="get_quiz"),
    path('api/submit_quiz/', views.submit_quiz, name="submit_quiz"),
    path('quiz/', views.quiz, name="quiz"),
    path('result/', views.result, name="result")
]
