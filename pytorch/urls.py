from django.urls import path
from . import views

urlpatterns = [
    path("", views.pytorch, name="pytorch"),
    path("<str:pk>/", views.pytorch_job, name="pytorch_job"),
]
