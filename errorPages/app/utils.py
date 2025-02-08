from django.conf import settings
import requests as rq

GOOGLE_SEARCH_API = getattr(settings, 'GOOGLE_SEARCH_API', '')
ID_SEARCH_ENGINE = getattr(settings, 'ID_SEARCH_ENGINE', '')

def google_search(query):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': GOOGLE_SEARCH_API,
        'cx': ID_SEARCH_ENGINE,
        'q': query
    }

    response = rq.get(url, params=params)
    return response.json()
