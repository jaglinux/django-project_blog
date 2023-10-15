from django.shortcuts import render
from django.http import HttpResponse
from .models import PytorchJob

# Create your views here.
def pytorch(request):
    pytorchJob = PytorchJob.objects.create(job_out = "Running job ")
    pytorchJob.save()
    return HttpResponse("Pytorch home page")

def pytorch_job(request, pk):
    return HttpResponse(f"Pytorch job page {pk}")