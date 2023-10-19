from django.urls import path
from . import views

urlpatterns = [
    path('sample/', views.sample, name='sample'),
    path('createdb/', views.createdb, name='createdb'),
    path('players/<int:page_number>/', views.players_list, name='players'),
    path('table/<int:page_number>/', views.players_table, name='players table'),
    path('player_details/<int:player_id>', views.player_details, name='player details'),
    path('teams/', views.teams, name='teams'),
    path('teams/roster/<str:team_name>/', views.teams_roster, name='teams roster'),
    path('search_players/', views.search_players, name='search players'),
]