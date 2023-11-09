from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import JobOffer
from .serializers import JobOfferSerializer

# Create your views here.
class JobListCreateAPIView(APIView):

    def get(self, request):
        jobs = JobOffer.objects.filter(available=True)
        serializer = JobOfferSerializer(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = JobOfferSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class JobDetailEditDeleteAPPIView(APIView):

    def get_object(self, pk):
        job = get_object_or_404(JobOffer, pk=pk)
        return job

    def get(self, request, pk):
        job = self.get_object(pk=pk)
        serializer = JobOfferSerializer(job)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        job = self.get_object(pk=pk)
        data = request.data
        serializer = JobOfferSerializer(job, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        job = self.get_object(pk=pk)
        job.delete()
        return Response({"detail": "offer deleted"}, status=status.HTTP_204_NO_CONTENT)