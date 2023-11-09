from django.urls import path
from .views import JobListCreateAPIView, JobDetailEditDeleteAPPIView

urlpatterns = [
    path("jobs/", JobListCreateAPIView.as_view(), name="jobs-list"),
    path("jobs/<int:pk>", JobDetailEditDeleteAPPIView.as_view(), name="job-detail"),
]
