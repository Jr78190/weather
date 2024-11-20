# le ficher urls.py permet d'importer les views.py necessaire afin d'associer les URLS
# importation de include pour importer d'autre URLS

from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('listings.urls') ),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
