from django.contrib import admin
from .models import Pokemon


class PokemonAdmin (admin.ModelAdmin):
    list_display = ('id', 'name', 'hp', 'active')
    list_filter = ('active',)
    fieldsets = (
        (None, {
            'fields': ('name', 'pokemon_type', 'hp', 'active')
        }),
        ('Localizations', {
            'classes': ('collapse',),
            'fields': ('name_fr', 'name_ar', 'name_jp'),
        }),
    )


# Register your models here.
admin.site.register(Pokemon, PokemonAdmin)
