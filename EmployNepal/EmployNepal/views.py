from django.shortcuts import render
from courseworkapp.models import Job


def index(request):
    Job_obj = Job.objects.all()
    print(Job_obj)
    context_varible = {
        'Jobs':Job_obj
    }
    return render(request,'index.html',context_varible)



def view_Jobdata_delete(request, ID):
    print(ID)
    Job_obj = Job.objects.get(id=ID)
    print(Job_obj)
    Job_obj.delete()
    return render(request,'')

def view_update_PostJob(request,ID):
    Job_obj = Job.objects.get(id=ID)
    print(Job_obj)
    job_post = request.POST
    print(job_post)
    Job_obj.job_Title = request.POST['job_Title']
    Job_obj.job_discription =request.POST['job_discription']
    Job_obj.job_Catagory = request.POST['job_Catagory']
    Job_obj.save()
    return render(request,'')