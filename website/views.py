from django.shortcuts import render
from .models import Player, MainPlayer

# Create your views here.

def sample(request):
    records = Player.objects.all()

    return render(request, 'sample.html', {'records': records})


def createdb(request):
    # Use the below as a one-off to insert all records from the dataset.txt file into the project database
    if not MainPlayer.objects.all():
        mydb = []
        with open('datasets\dataset.txt', 'r') as file:
            data = file.readlines()

            for idx, row in enumerate(data):
                player_data = [idx]
                player_data += row.strip().split(',')
                player_data[6] = int(player_data[6])
                player_data[17] = int(player_data[17])
                player_data = [float(el) if 6 < idx < 17 else el for idx, el in enumerate(player_data)]
                p = MainPlayer(*player_data)
                mydb.append(p)
            
        MainPlayer.objects.bulk_create(mydb)
    
    records = MainPlayer.objects.all()
    context = {'records': records}
    return render(request, 'players.html', context=context)


def players_list(request, page_number):
    rows_per_page = 30
    end_idx = page_number * rows_per_page
    start_idx = end_idx - rows_per_page
    records = MainPlayer.objects.all()[start_idx:end_idx]
    context = {
        'records': records,
        'page_number': page_number
    }

    return render(request, 'players.html', context=context)
