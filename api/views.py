from .models import Proizvod,Prodavnica
from rest_framework import viewsets
from .serializers import ProdavnicaSerializer, ProizvodSerializer
from rest_framework.permissions import IsAuthenticated


class ProdavnicaViewSet(viewsets.ModelViewSet):
    queryset = Prodavnica.objects.all()
    serializer_class = ProdavnicaSerializer
    permission_classes = [IsAuthenticated]

class ProizvodViewSet(viewsets.ModelViewSet):
    queryset = Proizvod.objects.all()
    serializer_class = ProizvodSerializer
    permission_classes = [IsAuthenticated]