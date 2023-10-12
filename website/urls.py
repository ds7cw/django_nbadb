from django.urls import path
from . import views

urlpatterns = [
    path('sample/', views.sample, name='sample'),
    path('createdb/', views.createdb, name='createdb'),
    path('players/<int:page_number>/', views.players_list, name='players'),
    path('table/<int:page_number>/', views.players_table, name='players table'),
]