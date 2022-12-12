from django.contrib import admin
from django.urls import path

from recipies.views import my_home

urlpatterns = [
    path('', my_home),
]
