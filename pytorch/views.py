from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import PytorchJob
from .tasks import run_pytorch

# Create your views here.
def pytorch(request):
    pytorchJob = PytorchJob.objects.create()
    pytorchJob.job_out = f"Running job with id {pytorchJob.id}"
    pytorchJob.save()
    return redirect(pytorch_job, pytorchJob.id)

def pytorch_job(request, pk):
    pytorchJob = get_object_or_404(PytorchJob, pk=pk)
    run_pytorch.delay(pk)
    return HttpResponse(f"{pytorchJob.job_out}")