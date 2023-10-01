from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("room/", views.room, name="room"),
    path("test_thread/", views.test_thread, name="test_thread"),
]
