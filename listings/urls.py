# le ficher urls.py permet d'importer les views.py necessaire afin d'associer les URL
from django.urls import path
from listings import views


urlpatterns = [
    path('', views.index),
]
