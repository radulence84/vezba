from django.test import TestCase
from .models import Prodavnica,Proizvod

class ProdavnicaModelTest(TestCase):
    def setUp(self):
        #kreiramo testni objekat
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
        #kreiramo testni objekat
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
