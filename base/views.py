from django.shortcuts import render
from django.http import HttpResponse
import threading
import time

# Create your views here.

def home(request):
    print("home request is ", request)
    print("home request thread is ", threading.get_native_id())
    return HttpResponse("Jag home page")

def room(request):
    print("room request is ", request)
    print("room request thread is ", threading.get_native_id())
    return HttpResponse("Jag Room")

def test_thread(request):
    print("test_thread request is ", request)
    print("thread sleep start ", threading.get_native_id())
    time.sleep(20)
    print("thread sleep end ", threading.get_native_id())
    return HttpResponse("Test_thread")