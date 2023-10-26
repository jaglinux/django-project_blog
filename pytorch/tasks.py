from celery import shared_task
import torch

@shared_task()
def run_pytorch(job_id):
    print(f"[{job_id}]: torch cuda ", torch.cuda.is_available())