from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

from .models import Greeting

# Create your views here.
def index(request):
    
    # api-endpoint 
    URL = "https://covid2019-api.herokuapp.com/country/italy"

    # sending get request and saving the response as response object 
    r = requests.get(url = URL) 

    # extracting data in json format 
    data = r.json() 
    
    text = 'Ultimo aggiornamento: {}\n Numero casi: {}\n Numero decessi: {} \n Numero guariti: {} \n Mappa dettagliata: https://bit.ly/38TTenD'.format(data['dt'], data['Italy']['confirmed'], data['Italy']['deaths'], data['Italy']['recovered'])

    return HttpResponse(text)
    """
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)
    """


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
