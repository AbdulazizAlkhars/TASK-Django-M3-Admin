from random import choices
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Pokemon(models.Model):
    class PokemonType(models.TextChoices):
        WATER = 'WA', ('WATER')
        GRASS = 'GR', ('GRASS')
        GHOST = 'GH', ('GHOST')
        STEEL = 'ST', ('STEEL')
        FAIRY = 'FA', ('FAIRY')

    def is_upperclass(self):
        return self.pokemon_type in {
            self.PokemonType.JUNIOR,
            self.PokemonType.SENIOR,
        }
    name = models.CharField(max_length=30)
    pokemon_type = models.CharField(
        max_length=2,
        choices=PokemonType.choices,
        default=PokemonType.WATER,
    )
    hp = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    name_fr = models.CharField(max_length=30, blank=True, null=True)
    name_ar = models.CharField(max_length=30, blank=True, null=True)
    name_jp = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
