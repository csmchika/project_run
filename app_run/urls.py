from django.contrib import admin
from django.urls import path, include
from .views import company_details_view

urlpatterns = [
    path('company_details/', company_details_view),
]
