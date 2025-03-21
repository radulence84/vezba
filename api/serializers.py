from .models import Prodavnica, Proizvod
from rest_framework import serializers

class ProdavnicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prodavnica
        fields = ['id','naziv_prodavnice','lokacija_prodavnice']

class ProizvodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proizvod
        fields = ['id','naziv_proizvoda','opis','cena','prodavnica']