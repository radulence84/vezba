
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdavnicaViewSet, ProizvodViewSet

router = DefaultRouter()
router.register(r'prodavnica', ProdavnicaViewSet, basename="prodavnica")
router.register(r'proizvod', ProizvodViewSet, basename="proizvod")

urlpatterns = [
    path('', include(router.urls)),
]