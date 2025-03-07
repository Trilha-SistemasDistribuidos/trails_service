from rest_framework import generics
from .models import Trail
from .serializers import TrailSerializer

class TrailCreateListView(generics.ListCreateAPIView):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer

class TrailRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer