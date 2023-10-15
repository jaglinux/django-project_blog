import time
from celery import shared_task

@shared_task()
def celery_test_worker(a=10):
    print("entering celery_test_worker")
    print(f"sleeping for {a} seconds")
    time.sleep(a)
    print("exiting celery_test_worker")
