from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Exercice(BaseEntity):
    name = models.CharField(max_length = 100)
    exo_file = models.FileField(upload_to='media',blank=False)

    def __str__(self):
    	return self.exo_file