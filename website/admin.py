from django.contrib import admin

# Register your models here.
from .models import Player, MainPlayer

admin.site.register(Player)
admin.site.register(MainPlayer)
