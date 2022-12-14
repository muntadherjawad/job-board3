from django.db import models

# Create your models here.
JOB_TYPE= (
    ('full time','full time'),
    ('part time','part time'),

)
class job(models.Model) :
    title = models.CharField(max_length=100,default='PROGRAMMER')
    #LOCATION
    job_type = models.CharField(max_length=100 , choices=JOB_TYPE ,default='full time')
    descrption = models.TextField(max_length=1000,null=True, default='Automatically set the field to now when the object is first created.')
    published_at =models.DateField(auto_now=True)
    vanacy = models.IntegerField(default=1)
    salary =models.IntegerField (default=0)
    experiance = models.IntegerField(default=1)
    category = models.ForeignKey('category',on_delete=models.CASCADE)

    def __str__(self):
         return (self.title)

class category(models.Model):
        name = models.CharField(max_length=25)     
        def __str__(self):
            return (self.name)
