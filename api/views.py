from django.http import QueryDict
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Proizvod, Prodavnica
from .serializers import ProdavnicaSerializer, ProizvodSerializer


class ProdavnicaViewSet(viewsets.ModelViewSet):
    queryset = Prodavnica.objects.all()
    serializer_class = ProdavnicaSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    # CREATE action
    def create(self, request, *args, **kwargs):
        """Create"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # LIST action§
    def list(self, request, *args, **kwargs):
        """List """
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # RETRIEVE action
    def retrieve(self, request, *args, **kwargs):
        """Retrieve """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """Update instance"""
        partial = kwargs.pop("partial", True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_update(serializer)
        response_data = self.get_serializer(instance).data
        return Response(response_data)

    def perform_update(self, serializer):
        """Perform update instance"""
        return  serializer.save()

class ProizvodViewSet(viewsets.ModelViewSet):
    queryset = Proizvod.objects.all()
    serializer_class = ProizvodSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    # CREATE action
    def create(self, request, *args, **kwargs):
        """Create"""
        payload = request.data

        # If your payload is a QueryDict
        if isinstance(payload, QueryDict):
            payload = dict(payload.items())

        # payload["promo_cena"] = int(payload["cena"]) * 0.9
        payload["created_by"] = request.user
        serializer = self.get_serializer(data=payload)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            raise e
        self.perform_create(serializer)
        print("napravio sam novi proizvod")
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # LIST action§
    def list(self, request, *args, **kwargs):
        """List """
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # RETRIEVE action
    def retrieve(self, request, *args, **kwargs):
        """Retrieve """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """Update instance"""
        partial = kwargs.pop("partial", True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_update(serializer)
        response_data = self.get_serializer(instance).data
        return Response(response_data)

    def perform_update(self, serializer):
        """Perform update instance"""
        return serializer.save()