from django.shortcuts import render
from django.http import HttpResponse
from .models import Job

def create_job(request):
    return render(request,'create_job.html')
    

def save(request):
    if request.method == "POST":
        get_all = request.POST
        get_job_Title = request.POST['job_Title']
        print(get_job_Title)
        get_job_discription = request.POST['job_discription']
        get_job_Catagory = request.POST['job_Catagory']
        print( get_job_Catagory)
        Job_obj = Job(job_Title=get_job_Title,job_discription=get_job_discription,job_Catagory=get_job_Catagory)
        Job_obj.save()
        return render(request,'index.html')
    else:
        return HttpResponse("Error record saving")


