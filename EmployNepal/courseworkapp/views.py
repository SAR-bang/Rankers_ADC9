from django.shortcuts import render
from django.http import HttpResponse
from .models import Resume
from django.core.files.storage import FileSystemStorage

# Create your views here.

def upload_Resume(request):
    return render(request, 'resume.html')

def save_Resume(request):
    context = {}
    if request.method == 'POST':
        get_resume = request.FILES['Resume']
        get_image = request.FILES['imageQR']
        get_name = request.POST['filename']
        get_user = request.POST['username']
        fs = FileSystemStorage()

        name_resume = fs.save(get_resume.name, get_resume)
        name_image = fs.save(get_image.name, get_image)
        
        print(fs.url(name_resume))

        form = Resume( name = get_name, user = get_user  , resume = get_resume, resume_QRcode = get_image)
        form.save()

    else:
        form = Resume()
    return render(request, 'resume.html', {'form':form})


def resumes_list(request):
    pdfs = Resume.objects.all()
    context = {
        'pdfs' : pdfs
    }
    return render(request, 'resumelist.html',context)


def searchResume(request):
    resumetitle = request.GET['Search']

    obj = Resume.objects.filter(name = resumetitle)

    print(obj)

    return render(request, 'resumelist.html', {'pdfs':obj})
