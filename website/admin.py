from django.contrib import admin

# Register your models here.
from .models import Player, MainPlayer

admin.site.register(Player)
# admin.site.register(MainPlayer)

@admin.register(MainPlayer)
class MainPlayerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'suffix',
                    'pos', 'team', 'rpg', 'apg', 'ppg'
                    ]
    search_fields = ['first_name', 'last_name', 'suffix']
    list_filter = ['team', 'pos']
