from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('pay', Pay.as_view(), name="pay"),
]