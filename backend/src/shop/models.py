from django.db import models

# Create your models here.
class Tissu(models.Model):
   # image = *models.ImageField(upload_to='image/')
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.PositiveIntegerField()
    nombre_de_metres = models.PositiveIntegerField()
    disponibilite_tissu = models.BooleanField(default=True)
    date_achat = models.DateField()

    def __str__(self):
        return self.nom

class Utilisateur(models.Model):
    nom = models.CharField(max_length=70)
    prenom = models.CharField(max_length=70)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=20)

    

    def __str__(self):
        return self.nom