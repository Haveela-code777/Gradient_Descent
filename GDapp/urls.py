from django.urls import path
from .views import gd, home

urlpatterns = [
    path('',home),
    path('result/',gd),
]
