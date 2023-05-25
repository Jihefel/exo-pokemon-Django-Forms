from django.db import models

class Pokemon(models.Model):
    nom = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    niveau = models.IntegerField()

    class Meta:
        db_table = 'pokemons'
