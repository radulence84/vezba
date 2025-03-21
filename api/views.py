from .models import Proizvod,Prodavnica
from rest_framework import viewsets
from .serializers import ProdavnicaSerializer, ProizvodSerializer

class ProdavnicaViewSet(viewsets.ModelViewSet):
    queryset = Prodavnica.objects.all()
    serializer_class = ProdavnicaSerializer

class ProizvodViewSet(viewsets.ModelViewSet):
    queryset = Proizvod.objects.all()
    serializer_class = ProizvodSerializer