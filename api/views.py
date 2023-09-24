from rest_framework import viewsets

from .models import *
from .serializers import *


# Create your views here.
class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animals.objects.all()
    serializer_class = AnimalSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breeds.objects.prefetch_related("animal").all()
    serializer_class = BreedSerializer


class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.prefetch_related("breed__animal").all()
    serializer_class = InfoSerializer
