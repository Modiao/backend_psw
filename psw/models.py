from django.db import models
from simple_history.models import HistoricalRecords
# Create your models here.

NIVEAU =(
    (1, "Sixieme College"),
    (2, "Cinquieme College"),
    (4, "Quatrieme College"),
    (5, "troisieme College"),
    (6, "Seconde Lycee"),
    (7, "Premiere Lycee"),
    (0, "Terminale Lycee"),
)
class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Exercice(BaseEntity):
    name = models.CharField(max_length = 100)
    exo_file = models.ImageField(upload_to='media',blank=True, null=True)
    niveau  = models.CharField(max_length = 6, choices = NIVEAU, default=0)
    description = models.TextField(blank= True)
    historique = HistoricalRecords()

    def __str__(self):
        return str(self.name) + str(self.niveau)