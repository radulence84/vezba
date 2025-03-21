from .models import Prodavnica, Proizvod
from rest_framework import serializers

class ProdavnicaSerializer(serializers.ModelSerializer)
    class Meta:
        model = Prodavnica
        fields = ['naziv_prodavnice','lokacija_prodavnice']

class ProizvodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proizvod
        fields = ['naziv_proizvoda','opis','cena']