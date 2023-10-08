from django.urls import path
from . import views

urlpatterns = [
    path('sample/', views.players, name='sample'),
    path('createdb/', views.createdb, name='createdb'),
]