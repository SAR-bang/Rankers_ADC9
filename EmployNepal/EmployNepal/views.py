from django.shortcuts import render
from courseworkapp.models import Job


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
        return render(request,'create_job.html')

def index(request):
    Job_obj = Job.objects.all()
    print(Job_obj)
    context_varible = {
        'Jobs':Job_obj
    }
    return render(request,'index.html',context_varible)


def view_Jobdata_delete(request, ID):
    print(ID)
    Jobs= Job.objects.get(id=ID)
    print(Jobs)
    Jobs.delete()
    return render(request,"index.html") 

def view_Jobdata_updateform(request,ID):
    print(ID)
    Jobs= Job.objects.get(id=ID)
    print(Jobs)
    context_varible = {
        'Job':Jobs
    }
    return render(request,'update_job.html',context_varible)

def view_update_PostJob(request,ID):
    Jobs = Job.objects.get(id=ID)
    print(Jobs)
    Jobs = request.POST
    print(Jobs)
    Jobs.job_Title = request.POST['job_Title']
    Jobs.job_discription =request.POST['job_discription']
    Jobs.job_Catagory = request.POST['job_Catagory']
    Jobs.save()
    return HttpResponse("Record Updated!!")
