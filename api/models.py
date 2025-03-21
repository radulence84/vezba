from django.db import models

class Prodavnica(models.Model):
    naziv_prodavnice = models.CharField(max_length=50)
    lokacija_prodavnice = models.CharField(max_length=50)

    def __str__(self):
        return self.naziv_prodavnice

class Proizvod(models.Model):
    naziv_prozvoda = models.CharField(max_length=50)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=4 , decimal_places=2)
    prodavnica = models.ForeignKey('Prodavnica', on_delete=models.CASCADE)

    def __str__(self):
        return self.naziv_prozvoda

