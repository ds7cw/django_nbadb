from django.shortcuts import render
from .models import Player

# Create your views here.

def players(request):
    records = Player.objects.all()

    return render(request, 'players.html', {'records': records})