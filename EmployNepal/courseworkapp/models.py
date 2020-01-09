from django.db import models

class Job(models.Model):
    job_Title= models.CharField(max_length=40)
    job_discription=models.CharField(max_length=100)
    job_Catagory= models.CharField(max_length=40)

    def __str__(self):
        return self.job_Title + " " + self.job_discription+" "+ self.job_Catagory

