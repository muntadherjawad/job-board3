from django.shortcuts import render
from .models import job
# Create your views here.


def job_list(request):
    jop_list = job.objects.all()
    return render (request,job_list.html,)

def job_detail(request ,id):
    pass