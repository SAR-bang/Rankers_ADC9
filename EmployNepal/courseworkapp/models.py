from django.db import models
# Create your models here.

class Resume(models.Model):
    name = models.CharField(max_length = 50)
    user = models.CharField(max_length = 50)
    resume = models.FileField(upload_to= 'resume/pdfs')
    resume_QRcode = models.ImageField(upload_to = 'resume/images', null=True, blank = True)


    def __str__(self):
        return f"  the resume name is {self.name} "