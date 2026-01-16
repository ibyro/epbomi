from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Invites(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\d{2}(-\d{2}){4}$',
        message="Le numéro doit être au format 05-05-05-05-05"
    )

    nom = models.CharField(max_length=60)
    prenom = models.CharField(max_length=120)
    telephone = models.CharField(
        max_length=14,
        validators=[phone_regex]
    )
    dateinvitation = models.DateTimeField()
    commune = models.CharField(max_length=100)
    quartier = models.CharField(max_length=120)
    invitepar = models.CharField(max_length=150)
    motifdepresence = models.CharField(max_length=200)
    communauteorigine = models.CharField(max_length=200)
    ministere   =models.CharField(max_length=100)
    Activitepro = models.CharField(max_length=100)
    sitmatrimoniale = models.CharField(max_length=40)
    groupesanguin = models.CharField(max_length=3)
    photo = models.ImageField(
        upload_to='invites/photos',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    