from django.urls import path
from .views import *

urlpatterns = [
    path('uploadResume/', upload_Resume, name='uploadResume'),
    path('uploadResume/savedata', save_Resume),
    path('uploadResume/download',resumes_list),
    path('uploadResume/search',searchResume),
    path('uploadResume/download/search',searchResume),
    path('uploadResume/savedata/search',searchResume),
]