from django.shortcuts import render
from rest_framework import generics, permissions
from .models import JobDescription
from .serializers import JobDescriptionSerializer

# Create your views here.
class JobDescriptionListCreateView(generics.ListCreateAPIView):
    queryset = JobDescription.objects.all()
    serializer_class = JobDescriptionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class JobDescriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobDescription.objects.all()
    serializer_class = JobDescriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

