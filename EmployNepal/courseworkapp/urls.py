from django.shortcuts import render

from django.urls import path,include
from .views import *
from EmployNepal.views import *

urlpatterns = [
    path('createjob/', create_job, name='create_job'),
    path('createjob/save', save),
    path('showJob/',index),
]