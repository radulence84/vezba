from django.test import TestCase
from .models import Prodavnica,Proizvod
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse

class KorisnikModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword')
        self.access_token = str(AccessToken.for_user(self.user))
        self.client = APIClient()
    def test_napravi_prodavnicu(self):
        payload = {
            "naziv_prodavnice": "Test Prodavnica",
            "lokacija_prodavnice": "Test Lokacija"
        }
        prodavnica_url = reverse("prodavnica-list")
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = self.client.post(prodavnica_url, payload, format="json", headers=headers)
        self.assertEqual(response.status_code, 201)

        self.assertEqual(Prodavnica.objects.count(), 1)
        db_prodavnica = Prodavnica.objects.get(id=response.data["id"])
        self.assertEqual(db_prodavnica.naziv_prodavnice, "Test Prodavnica")
        self.assertEqual(db_prodavnica.lokacija_prodavnice, "Test Lokacija")

class ProdavnicaModelTest(TestCase):
    def setUp(self):
        self.prodavnica = Prodavnica.objects.create(
            naziv_prodavnice = "Test Prodavnica",
            lokacija_prodavnice = "Test Lokacija"
        )

    def test_prodavnica_kreiranje(self):
        self.assertEqual(self.prodavnica.naziv_prodavnice, "Test Prodavnica")
        self.assertEqual(self.prodavnica.lokacija_prodavnice, "Test Lokacija")
        self.assertTrue(isinstance(self.prodavnica, Prodavnica))

    def test_prodavnica_str_metoda(self):
        self.assertEqual(str(self.prodavnica), "Test Prodavnica")

    def test_prodavnica_polja(self):
        self.assertEqual(self.prodavnica._meta.get_field('naziv_prodavnice').max_length, 50)
        self.assertEqual(self.prodavnica._meta.get_field('lokacija_prodavnice').max_length, 50)

class ProizvodModelTest(TestCase):
    def setUp(self):
        self.prodavnica = Prodavnica.objects.create(
            naziv_prodavnice = "Test Prodavnica",
            lokacija_prodavnice = "Test Lokacija"
        )

        self.proizvod = Proizvod.objects.create(
            naziv_proizvoda="Test Proizvod",
            opis="Test Opis",
            cena=100.00,
            prodavnica=self.prodavnica
        )

    def test_proizvod_kreiranje(self):
        self.assertEqual(self.proizvod.naziv_proizvoda, "Test Proizvod")
        self.assertEqual(self.proizvod.opis, "Test Opis")
        self.assertEqual(self.proizvod.cena, 100.00)
        self.assertEqual(self.proizvod.prodavnica, self.prodavnica)

    def test_proizvod_str_metoda(self):
        self.assertEqual(str(self.proizvod), "Test Proizvod")

    def test_proizvod_polja(self):
        self.assertEqual(self.proizvod._meta.get_field('naziv_proizvoda').max_length, 50)
        self.assertEqual(self.proizvod._meta.get_field('cena').max_digits, 10)
        self.assertEqual(self.proizvod._meta.get_field('cena').decimal_places, 2)
        self.assertEqual(self.proizvod._meta.get_field('prodavnica').related_model, Prodavnica)
